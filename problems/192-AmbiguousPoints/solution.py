class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        def generate(coord: str) -> str:
            if len(coord) == 1 or coord[0] != '0':
                yield coord
            if len(coord) > 1 and coord[-1] != '0':
                if coord[0] == '0':
                    yield f"{coord[0]}.{coord[1:]}"
                else:
                    yield from (f"{coord[:i]}.{coord[i:]}" for i in range(len(coord) - 1, 0, -1))

        return [f"({x}, {y})"
                for part1, part2 in ((S[1:i], S[i:-1]) for i in range(2, len(S) - 1))
                for x in generate(part1) for y in generate(part2)]