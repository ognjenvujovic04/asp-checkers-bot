 def calucalte_heuristic(self):
        whites = [0, 0, 0, 0, 0, 0, 0]
        blackes = [0, 0, 0, 0, 0, 0, 0]

        for r in range(8):
            for c in range(8):
                checker = self.pieces[r][c]
                if checker == CellState.EMPTY:
                    continue
                if checker in [CellState.WHITE, CellState.WHITE_QUEEN]:
                    if checker == CellState.WHITE:
                        whites[0] += 1
                    else:
                        whites[1] += 1
                    if r == 7:
                        whites[2] += 1
                        whites[6] += 1
                        continue
                    if r == 3 or r == 4:
                        if 2 <= c <= 5:
                            whites[3] += 1
                        else:
                            whites[4] += 1
                    if r > 0 and 0 < c < 7:
                        if self.pieces[r - 1][c - 1] in [CellState.BLACK, CellState.BLACK_QUEEN] and self.pieces[r + 1][c + 1] == CellState.EMPTY:
                            whites[5] += 1
                        if self.pieces[r - 1][c + 1] in [CellState.BLACK, CellState.BLACK_QUEEN] and self.pieces[r + 1][c - 1] == CellState.EMPTY:
                            whites[5] += 1
                    if r < 7:
                        if c == 0 or c == 7:
                            whites[6] += 1
                        elif (self.pieces[r + 1][c - 1] in [CellState.WHITE, CellState.WHITE_QUEEN] or self.pieces[r + 1][c - 1] not in [CellState.BLACK_QUEEN, CellState.WHITE_QUEEN]) and \
                        (self.pieces[r + 1][c + 1] in [CellState.WHITE, CellState.WHITE_QUEEN] or self.pieces[r + 1][c + 1] not in [CellState.BLACK_QUEEN, CellState.WHITE_QUEEN]):
                            whites[6] += 1
                else:
                    if checker == CellState.BLACK:
                        blackes[0] += 1
                    else:
                        blackes[1] += 1
                    if r == 0:
                        blackes[2] += 1
                        blackes[6] += 1
                        continue
                    if r == 3 or r == 4:
                        if 2 <= c <= 5:
                            blackes[3] += 1
                        else:
                            blackes[4] += 1
                    if r < 7 and 0 < c < 7:
                        if self.pieces[r + 1][c - 1] in [CellState.WHITE, CellState.WHITE_QUEEN] and self.pieces[r - 1][c + 1] == CellState.EMPTY:
                            blackes[5] += 1
                        if self.pieces[r + 1][c + 1] in [CellState.WHITE, CellState.WHITE_QUEEN] and self.pieces[r - 1][c - 1] == CellState.EMPTY:
                            blackes[5] += 1
                    if r > 0:
                        if c == 0 or c == 7:
                            blackes[6] += 1
                        elif (self.pieces[r - 1][c - 1] in [CellState.BLACK, CellState.BLACK_QUEEN] or self.pieces[r - 1][c - 1] not in [CellState.BLACK_QUEEN, CellState.WHITE_QUEEN]) and \
                        (self.pieces[r - 1][c + 1] in [CellState.BLACK, CellState.BLACK_QUEEN] or self.pieces[r - 1][c + 1] not in [CellState.BLACK_QUEEN, CellState.WHITE_QUEEN]):
                            blackes[6] += 1
        weights = [5, 7.5, 4, 2.5, 0.5, -3, 3]
        score = 0
        for i in range(7):
            score += weights[i] * (blackes[i] - whites[i])
        return score