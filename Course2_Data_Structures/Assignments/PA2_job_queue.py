# python3
import heapq

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        if self.num_workers >= len(self.jobs):
            for i in range(len(self.jobs)):
                self.assigned_workers[i] = i
                self.start_times[i] = 0
        else:
            next_free_time = []
            for i in range(self.num_workers):
                self.assigned_workers[i] = i
                self.start_times[i] = 0
                heapq.heappush(next_free_time, (self.jobs[i], i))
            for i in range(self.num_workers, len(self.jobs)):
                self.start_times[i], self.assigned_workers[i] = heapq.heappop(next_free_time)
                heapq.heappush(next_free_time, (self.start_times[i]+self.jobs[i], self.assigned_workers[i]))

        '''
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]
        '''

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

