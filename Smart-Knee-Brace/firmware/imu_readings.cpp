
#include <MPU6050.h>
MPU6050 imu;

void readIMU() {
    int16_t ax, ay, az;
    imu.getAcceleration(&ax, &ay, &az);
    // Processing logic here
}
