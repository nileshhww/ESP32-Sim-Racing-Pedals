// ===============================
// ESP32 Sim Pedals + 2 Buttons
// ===============================

#define THROTTLE_PIN 32
#define BRAKE_PIN    33

#define BUTTON1_PIN  18
#define BUTTON2_PIN  4

// Calibration
int throttleMin = 1980;
int throttleMax = 3200;

int brakeMin = 1980;
int brakeMax = 3200;

// Smoothing settings
const int samples = 10;

float throttleFiltered = 0;
float brakeFiltered = 0;

// ===============================

int readSmooth(int pin)
{
    long total = 0;

    for (int i = 0; i < samples; i++)
    {
        total += analogRead(pin);
    }

    return total / samples;
}

// ===============================

void setup()
{
    Serial.begin(115200);

    analogReadResolution(12);

    analogSetPinAttenuation(THROTTLE_PIN, ADC_11db);
    analogSetPinAttenuation(BRAKE_PIN, ADC_11db);

    pinMode(BUTTON1_PIN, INPUT_PULLUP);
    pinMode(BUTTON2_PIN, INPUT_PULLUP);

    delay(1000);
}

// ===============================

void loop()
{
    // Read hall sensors
    int throttleRaw = readSmooth(THROTTLE_PIN);
    int brakeRaw    = readSmooth(BRAKE_PIN);

    // Exponential smoothing
    throttleFiltered = throttleFiltered * 0.90 + throttleRaw * 0.10;
    brakeFiltered    = brakeFiltered * 0.90 + brakeRaw * 0.10;

    // Map to 16-bit axis values
    int throttle = map(
        constrain((int)throttleFiltered, throttleMin, throttleMax),
        throttleMin,
        throttleMax,
        0,
        65535
    );

    int brake = map(
        constrain((int)brakeFiltered, brakeMin, brakeMax),
        brakeMin,
        brakeMax,
        0,
        65535
    );

    // Buttons
    int button1 = !digitalRead(BUTTON1_PIN);
    int button2 = !digitalRead(BUTTON2_PIN);

    // Send:
    // Throttle,Brake,Button1,Button2
    Serial.print(throttle);
    Serial.print(",");

    Serial.print(brake);
    Serial.print(",");

    Serial.print(button1);
    Serial.print(",");

    Serial.println(button2);

    delay(20);
}
