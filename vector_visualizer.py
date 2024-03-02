import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
from vector import Vector
from vector_operations import VectorOperations
import os

class VectorVisualizer:
    def __init__(self, vectors):
        self.app = dash.Dash(__name__) # Create the Dash app
        self.vectors = vectors # Store the vectors
        self.sum_vector = Vector(0, 0, 0, 0) # Create a vector to store the sum of the vectors
        VectorOperations.sum_vectors(self.vectors, self.sum_vector) # Calculate the sum of the vectors
        self.setup_layout()
        self.setup_callbacks()

    # The setup_layout method creates the graph layout
    def setup_layout(self):
        self.app.layout = html.Div([
            dcc.Graph(
                id='my-graph',
                config={'editable': True}, # Enable the graph to be edited
                figure=self.generate_figure() # Generate the initial figure
            )
        ])

    # The setup_callbacks method sets up the callback to update the graph when the user moves a vector
    def setup_callbacks(self):
        @self.app.callback(
            Output('my-graph', 'figure'), # The output is the figure property of the graph
            Input('my-graph', 'relayoutData'), # The input is the relayoutData property of the graph
            prevent_initial_call=True # Prevent the callback from running when the app is first loaded
        )
        # The update_arrow function updates the graph when the user moves a vector
        def update_arrow(relayoutData):
            nonlocal self # Use the self variable from the outer scope
            # If the user moves the sum vector, update the sum vector's coordinates
            if 'shapes[0].x0' in relayoutData and 'shapes[0].y0' in relayoutData:
                # Calculate the change in x and y
                dx = round(relayoutData['shapes[0].x0']) - self.sum_vector.x0
                dy = round(relayoutData['shapes[0].y0']) - self.sum_vector.y0
                # Update the sum vector's coordinates
                self.sum_vector.x0 += dx
                self.sum_vector.y0 += dy
                self.sum_vector.x1 += dx
                self.sum_vector.y1 += dy
            # If the user moves a vector, update the vector's coordinates and recalculate the sum vector
            else:
                # Iterate over the vectors and update their coordinates
                # Start the index at 1 because the sum vector is at index 0
                for shape_idx, vector in enumerate(self.vectors, start=1):
                    base_key = f'shapes[{shape_idx}]' # Create the base key for the vector's coordinates
                    # If the user moves the vector, update the vector's coordinates
                    if f'{base_key}.x0' in relayoutData or f'{base_key}.x1' in relayoutData:
                        vector.x0 = round(relayoutData.get(f'{base_key}.x0', vector.x0))
                        vector.y0 = round(relayoutData.get(f'{base_key}.y0', vector.y0))
                        vector.x1 = round(relayoutData.get(f'{base_key}.x1', vector.x1))
                        vector.y1 = round(relayoutData.get(f'{base_key}.y1', vector.y1))
                VectorOperations.sum_vectors(self.vectors, self.sum_vector) # Recalculate the sum vector
            return self.generate_figure() # Return the updated figure

    # The generate_figure method generates the graph figure
    def generate_figure(self):
        # Create a list of shapes for the graph
        shapes = [
            {
                'type': 'line',
                'x0': self.sum_vector.x0,
                'y0': self.sum_vector.y0,
                'x1': self.sum_vector.x1,
                'y1': self.sum_vector.y1,
                'line': {'width': 3},
            }
        ] + [
            {
                'type': 'line',
                'x0': vector.x0,
                'y0': vector.y0,
                'x1': vector.x1,
                'y1': vector.y1,
                'line': {'width': 3},
            } for vector in self.vectors
        ]

        # Calculate the properties of the sum vector
        dx, dy, magnitude, angle = self.sum_vector.calculate_properties()

        return {
            'data': [], # No data is needed because the shapes are used to draw the vectors
            'layout': go.Layout(
                xaxis={
                    'range': [0, 50],
                    'autorange': False,
                    'dtick': 1,
                    'tickvals': [i for i in range(0, 51)],
                    'ticktext': [str(i) if i % 10 == 0 and i != 50 and i != -50 and i != 0 else '' for i in range(0, 51)],
                    'constrain': 'domain',
                },
                yaxis={
                    'range': [0, 50],
                    'autorange': False,
                    'dtick': 1,
                    'tickvals': [i for i in range(0, 51)],
                    'ticktext': [str(i) if i % 10 == 0 and i != 50 and i != -50 and i != 0 else '' for i in range(0, 51)],
                    'scaleanchor': 'x',
                    'scaleratio': 1,
                    'constrain': 'domain',
                },
                shapes=shapes, # Set the shapes to draw the vectors
                margin={'l': 50, 'b': 50, 't': 10, 'r': 10},
                hovermode='closest', # Enable the hover tool
                annotations=[
                    # Create an annotation to display the properties of the sum vector
                    {
                        'x': 20,
                        'y': 1,
                        'xref': 'x',
                        'yref': 'y',
                        'text': f"dx: {dx}, dy: {dy}, |v|: {magnitude:.2f}, θ: {angle:.2f}°",
                        'showarrow': False,
                        'font': {'size': 12},
                    }
                ],
            )
        }

    # The run method runs the Dash app
    def run(self):
        self.app.run_server(debug=True, port=(os.environ.get('PORT') or 8050))