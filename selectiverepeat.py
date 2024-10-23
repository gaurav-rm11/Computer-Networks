import time
import random

class SelectiveRepeat:
    def __init__(self, window_size, total_frames):
        self.window_size = window_size
        self.total_frames = total_frames
        self.next_frame_to_send = 0
        self.acks = [False] * total_frames

    def send_frame(self, frame):
        print(f"Sending frame {frame}")
        # Simulate network delay
        time.sleep(random.uniform(0.5, 1.5))

    def receive_ack(self, ack):
        # Simulate ACK reception with a chance of loss
        if random.random() > 0.1:  # 90% chance of successful ACK
            print(f"Received ACK for frame {ack}")
            return True
        else:
            print(f"ACK for frame {ack} lost.")
            return False

    def start(self):
        while self.next_frame_to_send < self.total_frames:
            # Send all frames in the window
            for i in range(self.window_size):
                if self.next_frame_to_send + i < self.total_frames:
                    self.send_frame(self.next_frame_to_send + i)

            # Wait for ACKs
            for i in range(self.window_size):
                if self.next_frame_to_send + i < self.total_frames:
                    ack_received = self.receive_ack(self.next_frame_to_send + i)
                    if ack_received:
                        self.acks[self.next_frame_to_send + i] = True

            # Move the window forward
            while self.acks[self.next_frame_to_send]:
                self.next_frame_to_send += 1

if __name__ == "__main__":
    protocol = SelectiveRepeat(window_size=3, total_frames=10)
    protocol.start()
