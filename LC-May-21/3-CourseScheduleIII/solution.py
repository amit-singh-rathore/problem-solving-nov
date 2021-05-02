class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])

        heap = []
        days_used = 0
        course_count = 0

        for duration, finsihby in courses:
            heapq.heappush(heap, -duration)
            days_used += duration
            if days_used > finsihby:
                days_used -= -heapq.heappop(heap)
                course_count -= 1
            course_count += 1

        return course_count