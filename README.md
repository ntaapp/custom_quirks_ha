
# Custom ZHA Quirks for TS0601 Curtain Motor

This guide helps you set up a custom ZHA quirk for the TS0601 curtain motor (e.g., _TZE200_cpbo62rn) in Home Assistant, allowing basic curtain control without a Tuya hub or remote.

---

## 1. File Structure

Ensure your files are organized as follows:

```
/config/
	└── custom_zha_quirks/
				└── ts0601_curtain.py
```

---

## 2. Update `configuration.yaml`

Add the following at the **top level** (not indented under anything else):

```yaml
zha:
	enable_quirks: true
	custom_quirks_path: /config/custom_zha_quirks
```

Your `configuration.yaml` might look like this:

```yaml
default_config:

zha:
	enable_quirks: true
	custom_quirks_path: /config/custom_zha_quirks

# Text to speech
tts:
	- platform: google_translate
```

This tells ZHA to load quirks from your custom folder.

---

## 3. Final Steps

1. **Restart Home Assistant**: Go to **Settings → System → Restart**.
2. **(Recommended)**: Remove and re-pair your curtain device so the new quirk is applied.

---

## 4. About the Quirk

If you have a TS0601 curtain motor by `_TZE200_cpbo62rn`, the provided quirk enables basic curtain controls. Just place the Python file in your custom quirks folder as shown above.

This is based on the standard ZHA quirk for similar devices, with a single line added to support this model:

```python
("_TZE200_cpbo62rn", "TS0601"),
```

---

## 5. References & More Info

- [Reddit: Working ZHA quirk for Tuya Zigbee curtain](https://www.reddit.com/r/homeassistant/comments/1gk2z8d/working_zha_quirk_for_tuyazigbee_curtain/)
- [GitHub Issue: zigpy/zha-device-handlers #1245](https://github.com/zigpy/zha-device-handlers/issues/1245)
- [Example in zhaquirks/tuya/ts0601_cover.py](https://github.com/zigpy/zha-device-handlers/blob/9a1401337a25a4adc33e0b37ace62d808b7b3098/zhaquirks/tuya/ts0601_cover.py#L184)
