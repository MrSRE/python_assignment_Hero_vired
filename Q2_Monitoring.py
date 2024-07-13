import psutil
import time
def monitor_cpu(threshold=80):
    """
    Monitor the CPU usage and alert if it exceeds the specified threshold.    
    Args:
    threshold (int): The CPU usage percentage threshold for alerts.
    """
    print("Monitoring CPU usage...")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    monitor_cpu(threshold=80)