from vector import Vector
from vector_visualizer import VectorVisualizer
import os

vectors = [Vector(0, 0, 10, 10), Vector(0, 0, 20, 10)]
visualizer = VectorVisualizer(vectors)
app = visualizer.app  # Get the Dash app instance

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8050)))