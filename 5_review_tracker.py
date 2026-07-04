# Final Exam Review Progress Tracker (OOP Version)
# Complete object-oriented programming coursework
class ExamReviewProgress:
    def __init__(self, subject_name, total_chapters):
        self.subject = subject_name
        self.total_chap = total_chapters
        self.finished_chap = 0

    def finish_chapter(self, num):
        """Record finished review chapters"""
        self.finished_chap += num
        if self.finished_chap > self.total_chap:
            self.finished_chap = self.total_chap

    def get_progress_rate(self):
        """Calculate review completion percentage"""
        rate = (self.finished_chap / self.total_chap) * 100
        return round(rate, 2)

    def show_status(self):
        print(f"\nSubject: {self.subject}")
        print(f"Total chapters: {self.total_chap}, Finished: {self.finished_chap}")
        print(f"Review progress: {self.get_progress_rate()}%")

if __name__ == "__main__":
    # Create instances for different courses
    acc = ExamReviewProgress("Accounting", 12)
    math = ExamReviewProgress("Calculus", 10)
    # Record finished content
    acc.finish_chapter(7)
    math.finish_chapter(4)
    # Print progress report
    acc.show_status()
    math.show_status()