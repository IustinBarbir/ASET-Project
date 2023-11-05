# Observer Interface
class Observer:
    def update(self, message):
        pass

# Subject (or Publisher) Class
class DecodingSubject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

    def decode(self, matrix_type, matrix_data):
        # Perform Stern's ISD algorithm for decoding
        result = f"Decoding {matrix_type} matrix using Stern's ISD algorithm: {matrix_data}"
        self.notify_observers(result)

# Concrete Observer Implementations
class LoggingObserver(Observer):
    def update(self, message):
        print(f"LoggingObserver: {message}")

class EmailNotificationObserver(Observer):
    def update(self, message):
        # Implement email notification here
        print(f"EmailNotificationObserver: Email sent - {message}")

# Client code
def main():
    decoding_subject = DecodingSubject()
    logging_observer = LoggingObserver()
    email_observer = EmailNotificationObserver()

    decoding_subject.add_observer(logging_observer)
    decoding_subject.add_observer(email_observer)

    matrix_type = "sparse"  # Matrix type (sparse or dense)
    matrix_data = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]  # Your matrix data here

    decoding_subject.decode(matrix_type, matrix_data)

if __name__ == "__main__":
    main()
