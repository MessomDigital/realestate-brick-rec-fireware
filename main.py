import json
from source.fiware_converter import FiwareConverter

if __name__ == '__main__':
    sensor = {
        "id": "sensor-1",
        "name": "Temperature Sensor",
        "unit": "C",
        "value": 25.0,
        "isPointOf": {
            "id": "building-1"
        }
    }
    ngsi_ld_sensor = FiwareConverter.convert_sensor_to_ngsi_ld(sensor)
    print(ngsi_ld_sensor)
    with open('digital-twin-fiware.json', 'w') as f:
        json.dump(ngsi_ld_sensor, f, indent=2)