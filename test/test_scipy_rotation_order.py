from scipy.spatial.transform import Rotation as R

if __name__ == "__main__":
    r0 = R.from_euler('xyz', [40, 40, 40], degrees=True)
    r1 = R.from_euler('x', [40], degrees=True)
    r2 = R.from_euler('y', [40], degrees=True)
    r3 = R.from_euler('z', [40], degrees=True)
    result0 = r0.as_quat()
    result1 = (r3 * r2 * r1).as_quat()
    result0
    result1
    print(result0)
    print(result1)

