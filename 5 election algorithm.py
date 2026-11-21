class Process:
    def __init__(self, id):
        self.id = id
        self.act = True


class Election:
    def __init__(self):
        self.p = [Process(i) for i in range(5)]

    def run(self):
        self.p[4].act = False
        print("No of processes 5")
        print("Process no 4 fails")
        print("Election Initiated by 2")

        active = [p.id for p in self.p if p.act]
        active.sort()

        for i in range(2, 5):
            if self.p[i % 5].act:
                print(f"Process {i-1} pass Election({i-1}) to {i % 5}")

        coord = max(active)
        print(f"Process {coord} becomes coordinator")

        for i in range(coord + 1, coord + 5):
            if self.p[i % 5].act:
                print(f"Process {coord} pass Coordinator({coord}) message to process {i % 5}")

        print("End Of Election")


def main():
    Election().run()


if __name__ == "__main__":
    main()