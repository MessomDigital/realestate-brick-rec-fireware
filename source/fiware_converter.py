





class FiwareConverter:
    pass

    def convert_sensor_to_ngsi_ld(sensor):
        return {
            "id": f"urn:ngsi-ld:Sensor:{sensor['id']}",
            "type": "Sensor",
            "properties": {
                "name": {
                    "type": "Property",
                    "value": sensor["name"]
                },
                "unit": {
                    "type": "Property",
                    "value": sensor["unit"]
                },
                "value": {
                    "type": "Property",
                    "value": sensor["value"]
                }
            },
            "relationships": {
                "isPointOf": {
                    "type": "Relationship",
                    "object": f"urn:ngsi-ld:Building:{sensor['isPointOf']['id']}"
                }
            }
        }