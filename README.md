# Build Vars Spoofing

Build Vars Spoofing. **Android 8.1 or above is required**.

## Usage

1. Flash this module and reboot.
2. Enjoy!

You can try enabling/disabling Build variable spoofing by creating/deleting the file `/data/adb/boot_var_spoof/spoof_build_vars`.

Build Vars Spoofing will automatically generate example config props inside `/data/adb/boot_var_spoof/spoof_build_vars` once created, on next reboot, then you may manually edit your spoof config.

Here is an example of a spoof config:

```
MANUFACTURER=Google
MODEL=Pixel 9 Pro
FINGERPRINT=google/caiman/caiman:14/AD1A.240530.047.U1/12150698:user/release-keys
BRAND=google
PRODUCT=caiman
DEVICE=caiman
RELEASE=14
ID=AD1A.240530.047.U1
INCREMENTAL=12150698
TYPE=user
TAGS=release-keys
SECURITY_PATCH=2024-08-05
```

## Acknowledgement

- [PlayIntegrityFix](https://github.com/chiteroman/PlayIntegrityFix)
- [LSPosed](https://github.com/LSPosed/LSPosed)
