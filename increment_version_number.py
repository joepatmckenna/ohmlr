def increment_version_number():
    with open('version', 'r') as f:
        version = f.read()
    version = [int(v) for v in version.split('.')]
    base = [10, 10, 100]
    i = 2
    version[i] += 1
    while version[i] == base[i]:
        i -= 1
        version[i] += 1
    for j in range(i + 1, 3):
        version[j] = 0
    version = '.'.join([str(v) for v in version])
    with open('version', 'w') as f:
        f.write(version)


if __name__ == '__main__':
    increment_version_number()
