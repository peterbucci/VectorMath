from vector import Vector
from vector_visualizer import VectorVisualizer

# Initialize your vectors and the visualizer
vectors = [Vector(0, 0, 10, 10), Vector(0, 0, 20, 10)]
visualizer = VectorVisualizer(vectors)

# Get the Flask server from the Dash app instance for Gunicorn to use
app = visualizer.app  # app is the Dash app
server = visualizer.get_server()  # server is the Flask server that Gunicorn will interface with

if __name__ == "__main__":
    app.run_server(debug=True)
