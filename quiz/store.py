import csv


def save_attempt(file_path, attempt):
    
    try:
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([attempt.name, attempt.timestamp, attempt.score, attempt.total])
    except:
        print("Could not save attempt.")


def load_attempts(file_path):
    
    attempts = []

    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                attempts.append(row)
    except:
    
        return []

    return attempts