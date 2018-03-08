import json

if __name__ == '__main__':
    with open('test_log', 'w') as f:
        for i in range(100):
            msg = json.dumps({"message": i, "level": "DEBUG"})
            f.write(msg + '\n')
