from vector import Vector
from vector_visualizer import VectorVisualizer

def main():
    vectors = [Vector(0, 0, 10, 10), Vector(0, 0, 20, 10)]
    visualizer = VectorVisualizer(vectors)
    visualizer.run()

if __name__ == "__main__":
    main()
