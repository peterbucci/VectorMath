class VectorOperations:
    # This method calculates the sum of the vectors and stores the result in sum_vector
    @staticmethod
    def sum_vectors(vectors, sum_vector):
        sum_dx, sum_dy = 0, 0
        for vector in vectors:
            sum_dx += vector.x1 - vector.x0
            sum_dy += vector.y1 - vector.y0
        sum_vector.x1 = sum_vector.x0 + sum_dx
        sum_vector.y1 = sum_vector.y0 + sum_dy
