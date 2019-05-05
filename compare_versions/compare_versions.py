def compare_versions(version1: str, version2: str) -> int:
    version1, version2 = (map(int, v.split('.')) for v in [version1, version2])
    version1, version2 = zip(*map(lambda p1, p2: (p1 or 0, p2 or 0), version1, version2))

    for i in range(len(version1)):
        if version1[i] != version2[i]:
            return version1[i] - version2[i]
    return 0
