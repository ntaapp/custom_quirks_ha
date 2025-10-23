# Tuya mmWave radar 24GHz, _TZE204_gkfbdvyx
# Loginovo Smart Human Presence Sensor M100, Model C3007
# TZ-HS-24G Zigbee Ceiling 24G
(
    TuyaQuirkBuilder("_TZE204_gkfbdvyx", "TS0601")
    .tuya_dp(
        dp_id=1,
        ep_attribute=TuyaOccupancySensing.ep_attribute,
        attribute_name=OccupancySensing.AttributeDefs.occupancy.name,
        # 0: state="none", presence=false
        # 1: state="presence" presence=true
        # 2: state="move" presence=true
        converter=lambda x: True if x in (1, 2) else False,
    )
    .adds(TuyaOccupancySensing)
    .tuya_number(
        dp_id=2,
        attribute_name="move_sensitivity",
        type=t.uint16_t,
        min_value=0,
        max_value=10,
        step=1,
        translation_key="move_sensitivity",
        fallback_name="Motion sensitivity",
    )
    .tuya_number(
        dp_id=3,
        attribute_name="detection_distance_min",
        type=t.uint16_t,
        multiplier=0.1,
        device_class=SensorDeviceClass.DISTANCE,
        unit=UnitOfLength.METERS,
        min_value=0,
        max_value=6,
        step=0.5,
        translation_key="detection_distance_min",
        fallback_name="Minimum range",
    )
    .tuya_number(
        dp_id=4,
        attribute_name="detection_distance_max",
        type=t.uint16_t,
        multiplier=0.1,
        device_class=SensorDeviceClass.DISTANCE,
        unit=UnitOfLength.METERS,
        min_value=0,
        max_value=9,
        step=0.5,
        translation_key="detection_distance_max",
        fallback_name="Maximum range",
    )
    .tuya_sensor(
        dp_id=9,
        attribute_name="distance",
        type=t.uint16_t,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.DISTANCE,
        unit=UnitOfLength.METERS,
        multiplier=0.1,
        entity_type=EntityType.STANDARD,
        translation_key="target_distance",
        fallback_name="Target distance",
    )
    .tuya_switch(
        dp_id=101,
        attribute_name="find_switch",
        entity_type=EntityType.STANDARD,
        translation_key="distance_switch",
        fallback_name="Distance tracking",
    )
    .tuya_number(
        # L1-L5 ?
        dp_id=102,
        attribute_name="presence_sensitivity",
        type=t.uint16_t,
        min_value=1,
        max_value=10,
        step=1,
        translation_key="presence_sensitivity",
        fallback_name="Presence Sensitivity",
    )
    .tuya_illuminance(
        # confirmed via cluster 0x04000 reporting lumens?
        dp_id=103,
    )
    .tuya_enum(
        dp_id=104,
        attribute_name="motion_state",
        enum_class=TuyaPresenceState,
        entity_platform=EntityPlatform.SENSOR,
        entity_type=EntityType.STANDARD,
        translation_key="motion_state",
        fallback_name="Motion state",
    )

    .tuya_number(
        dp_id=105,
        attribute_name="presence_timeout",
        type=t.uint16_t,
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        min_value=1,
        max_value=1500,
        step=1,
        translation_key="fading_time",
        fallback_name="Fading time",
    )
    # Sensor fails when skip_configuration is enabled
    #.skip_configuration()
    .add_to_registry()
)
