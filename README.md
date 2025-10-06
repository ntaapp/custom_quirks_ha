
# Custom ZHA Quirks for TS0601 Curtain Motor and ts1201 IR blaster from Tuya

This guide helps you set up a custom ZHA quirk for the TS0601 curtain motor (e.g., _TZE200_cpbo62rn)and ts1201 IR blaster in Home Assistant, allowing basic curtain control and IR blaster without a Tuya hub or remote.

---

## 1. File Structure

Ensure your files are organized as follows:

```
/config/
	└── custom_zha_quirks/
				└── ts0601_curtain.py
                    ts1201.py
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

## 3. About the Quirk

If you have TS0601 curtain motor and ts1201 IR blaster by `_TZE200_cpbo62rn`, the provided quirk enables basic curtain controls. Just place the Python files in your custom quirks folder as shown above.
If you have a TS0601 with ID like this: _TZE200_cpbo62rn curtian motor, 
the below quirk will give you very basic curtain controls without 
needing a remote control or Tuya hub. Just stick this into ts0601_curtain.py 
file and use like any other quirk. 
This is the standard ZHA quirk file for similar items with a single
 line added at line 181 to support this device.

 ("_TZE200_cpbo62rn", "TS0601"), 

This is based on the standard ZHA quirk for similar devices, with a single line added to support this model:

```python
("_TZE200_cpbo62rn", "TS0601"),
```


The ts1201.py Quirk is for Supporting IR Blaster of Tuya IR Battery TS1201, you also need to add your device id similar to Curtain above
see this video to learn command https://www.youtube.com/watch?v=d1kkJpolE1w&t=3s
<img width="775" height="639" alt="image" src="https://github.com/user-attachments/assets/9c20ca8f-2dd3-47e2-87ac-a0423376c91b" />
<img width="959" height="788" alt="image" src="https://github.com/user-attachments/assets/bf095602-c2f2-46f1-a1f3-9908fdd88278" />
<img width="941" height="773" alt="image" src="https://github.com/user-attachments/assets/2494bcc8-7af9-4d47-9a8d-5e3b529b1e75" />



---

## 4. Final Steps

1. **Restart Home Assistant**: Go to **Settings → System → Restart**.
2. **(Recommended)**: Remove and re-pair your curtain device so the new quirk is applied.

---

## 5. References & More Info

- [Reddit: Working ZHA quirk for Tuya Zigbee curtain](https://www.reddit.com/r/homeassistant/comments/1gk2z8d/working_zha_quirk_for_tuyazigbee_curtain/)
- [GitHub Issue: zigpy/zha-device-handlers #1245](https://github.com/zigpy/zha-device-handlers/issues/1245)
- [Example in zhaquirks/tuya/ts0601_cover.py](https://github.com/zigpy/zha-device-handlers/blob/9a1401337a25a4adc33e0b37ace62d808b7b3098/zhaquirks/tuya/ts0601_cover.py#L184)
