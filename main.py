from vector import Vector
from vector_visualizer import VectorVisualizer

vectors = [Vector(0, 0, 10, 10), Vector(0, 0, 20, 10)]
visualizer = VectorVisualizer(vectors)
server = visualizer.get_server()  # This is the Flask server object

if __name__ == "__main__":
    visualizer.run()