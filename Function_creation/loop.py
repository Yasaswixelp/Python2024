def create_counter(n):

    def counter():
        result = []
        current = n
        for _ in range(3):
            result.append(current)
            current += 1
        return result

    return counter
