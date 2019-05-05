def compare_versions(version1: str, version2: str) -> int:
    """Compare 2 version strings

    :param version1: Version string; dot separated numbers; white spaces in between are not considered
    :param version2: Version string; dot separated numbers; white spaces in between are not considered
    :return:
        positive number: If the first version is greater than the second
        negative number: If the first version is smaller than the second
        zero: If the versions are equals
    """

    version1, version2 = (map(int, v.split('.')) for v in [version1, version2])
    version1, version2 = zip(*map(lambda p1, p2: (p1 or 0, p2 or 0), version1, version2))

    for i in range(len(version1)):
        if version1[i] != version2[i]:
            return version1[i] - version2[i]
    return 0
