import re

# Input string
#testString = "  Package [com.android.adservices.api] (a37eabe)"
# vim: set fdm=marker fmr={{{,}}} fdl=0 :
# {{{ dummy data
testString = """
  Package [org.proninyaroslav.libretorrent] (1e0e763):
    appId=10076
    pkg=Package{5a36244 org.proninyaroslav.libretorrent}
    codePath=/data/app/~~H-4fKmtR1gLG8IXeIY7WSg==/org.proninyaroslav.libretorrent-yZOLSlAHADAyHKQiDyceWw==
    resourcePath=/data/app/~~H-4fKmtR1gLG8IXeIY7WSg==/org.proninyaroslav.libretorrent-yZOLSlAHADAyHKQiDyceWw==
    legacyNativeLibraryDir=/data/app/~~H-4fKmtR1gLG8IXeIY7WSg==/org.proninyaroslav.libretorrent-yZOLSlAHADAyHKQiDyceWw==/lib
    extractNativeLibs=false
    primaryCpuAbi=arm64-v8a
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=26 minSdk=24 targetSdk=31
    minExtensionVersions=[]
    versionName=3.5-beta01
    usesNonSdkApi=false
    splits=[base]
    apkSigningVersion=3
    flags=[ HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVATE_FLAG_REQUEST_LEGACY_EXTERNAL_STORAGE HAS_DOMAIN_URLS PARTIALLY_DIRECT_BOOT_AWARE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    queriesIntents=[Intent { act=android.intent.action.SEND dat=content://*/... typ=message/rfc822 }, Intent { act=android.intent.action.SEND_MULTIPLE dat=content://*/... typ=message/rfc822 }, Intent { act=android.intent.action.SENDTO }]
    dataDir=/data/user/0/org.proninyaroslav.libretorrent
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    usesOptionalLibraries:
      androidx.window.extensions
      androidx.window.sidecar
    timeStamp=2024-03-11 23:16:14
    lastUpdateTime=2024-03-11 23:16:14
    installerPackageName=com.android.packageinstaller
    installerPackageUid=1110028
    initiatingPackageName=com.android.packageinstaller
    originatingPackageName=org.fdroid.fdroid
    packageSource=3
    appMetadataFilePath=null
    signatures=PackageSignatures{319bf2d version:3, signatures:[936027fe], past signatures:[]}
    installPermissionsFixed=true
    pkgFlags=[ HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVATE_FLAG_REQUEST_LEGACY_EXTERNAL_STORAGE HAS_DOMAIN_URLS PARTIALLY_DIRECT_BOOT_AWARE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    install permissions:
      android.permission.MANAGE_EXTERNAL_STORAGE: granted=false
      android.permission.FOREGROUND_SERVICE: granted=true
      android.permission.RECEIVE_BOOT_COMPLETED: granted=true
      android.permission.CHANGE_WIFI_STATE: granted=true
      android.permission.ACCESS_NETWORK_STATE: granted=true
      android.permission.SCHEDULE_EXACT_ALARM: granted=false
      android.permission.VIBRATE: granted=true
      android.permission.ACCESS_WIFI_STATE: granted=true
      com.android.launcher.permission.INSTALL_SHORTCUT: granted=true
      android.permission.WAKE_LOCK: granted=true
    User 0: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2024-03-11 23:16:14
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false
        android.permission.OTHER_SENSORS: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.READ_MEDIA_IMAGES: granted=false
        android.permission.READ_MEDIA_AUDIO: granted=false
        android.permission.READ_MEDIA_VIDEO: granted=false
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ APPLY_RESTRICTION]
    User 10: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false
        android.permission.OTHER_SENSORS: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.READ_MEDIA_IMAGES: granted=false
        android.permission.READ_MEDIA_AUDIO: granted=false
        android.permission.READ_MEDIA_VIDEO: granted=false
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ APPLY_RESTRICTION]
    User 11: ceDataInode=1643854 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=4
      firstInstallTime=2024-03-11 23:16:27
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.INTERNET: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
      disabledComponents:
        org.proninyaroslav.libretorrent.receiver.BootReceiver
      enabledComponents:
        androidx.work.impl.background.systemjob.SystemJobService
    User 13: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false
        android.permission.OTHER_SENSORS: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false
        android.permission.READ_MEDIA_IMAGES: granted=false
        android.permission.READ_MEDIA_AUDIO: granted=false
        android.permission.READ_MEDIA_VIDEO: granted=false
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false
    User 17: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false
        android.permission.OTHER_SENSORS: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false
        android.permission.READ_MEDIA_IMAGES: granted=false
        android.permission.READ_MEDIA_AUDIO: granted=false
        android.permission.READ_MEDIA_VIDEO: granted=false
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false
  Package [com.android.uwb.resources] (cd4df60):
    appId=10217
    pkg=Package{ae691f3 com.android.uwb.resources}
    codePath=/apex/com.android.uwb/priv-app/ServiceUwbResources@UP1A.231105.001
    resourcePath=/apex/com.android.uwb/priv-app/ServiceUwbResources@UP1A.231105.001
    legacyNativeLibraryDir=/apex/com.android.uwb/priv-app/ServiceUwbResources@UP1A.231105.001/lib
    extractNativeLibs=false
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=1 minSdk=33 targetSdk=34
    minExtensionVersions=[]
    versionName=T-initial
    usesNonSdkApi=false
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE DEFAULT_TO_DEVICE_PROTECTED_STORAGE DIRECT_BOOT_AWARE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    dataDir=/data/user_de/0/com.android.uwb.resources
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=1970-01-01 01:00:00
    lastUpdateTime=1970-01-01 01:00:00
    installerPackageName=null
    installerPackageUid=-1
    initiatingPackageName=null
    originatingPackageName=null
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{9965eb0 version:3, signatures:[4594e6f4], past signatures:[]}
    installPermissionsFixed=false
    pkgFlags=[ SYSTEM ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE DEFAULT_TO_DEVICE_PROTECTED_STORAGE DIRECT_BOOT_AWARE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=com.android.uwb
    User 0: ceDataInode=812239 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 10: ceDataInode=292808 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 11: ceDataInode=800469 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 13: ceDataInode=880344 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 17: ceDataInode=0 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true
  Package [com.android.internal.display.cutout.emulation.corner] (f4ac865):
    appId=10006
    pkg=Package{2deccae com.android.internal.display.cutout.emulation.corner}
    codePath=/product/overlay/DisplayCutoutEmulationCorner
    resourcePath=/product/overlay/DisplayCutoutEmulationCorner
    legacyNativeLibraryDir=/product/overlay/DisplayCutoutEmulationCorner/lib
    extractNativeLibs=true
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=1 minSdk=34 targetSdk=34
    minExtensionVersions=[]
    versionName=1.0
    usesNonSdkApi=false
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRODUCT PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    dataDir=/data/user/0/com.android.internal.display.cutout.emulation.corner
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=2009-01-01 00:00:00
    lastUpdateTime=2009-01-01 00:00:00
    installerPackageName=null
    installerPackageUid=-1
    initiatingPackageName=null
    originatingPackageName=null
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{7ce5a4f version:3, signatures:[4594e6f4], past signatures:[]}
    installPermissionsFixed=false
    pkgFlags=[ SYSTEM ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRODUCT PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    overlayTarget=android
    overlayCategory=com.android.internal.display_cutout_emulation
    User 0: ceDataInode=1349 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 10: ceDataInode=513758 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 11: ceDataInode=5147 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 13: ceDataInode=17743 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 17: ceDataInode=453396 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
  Package [app.vanadium.browser] (6f28c19):
    compat name=org.chromium.chrome
    appId=10085
    pkg=Package{fff09eb org.chromium.chrome}
    codePath=/data/app/~~FvgQQQbtM_0tF5kpM2dhog==/org.chromium.chrome-t5_tNzN1JwFEBh6Wjibdvg==
    resourcePath=/data/app/~~FvgQQQbtM_0tF5kpM2dhog==/org.chromium.chrome-t5_tNzN1JwFEBh6Wjibdvg==
    legacyNativeLibraryDir=/data/app/~~FvgQQQbtM_0tF5kpM2dhog==/org.chromium.chrome-t5_tNzN1JwFEBh6Wjibdvg==/lib
    extractNativeLibs=false
    primaryCpuAbi=arm64-v8a
    secondaryCpuAbi=armeabi-v7a
    cpuAbiOverride=null
    versionCode=631208133 minSdk=29 targetSdk=34
    minExtensionVersions=[]
    versionName=123.0.6312.80.1
    usesNonSdkApi=false
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA UPDATED_SYSTEM_APP ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION HAS_DOMAIN_URLS PARTIALLY_DIRECT_BOOT_AWARE PRODUCT PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    dataDir=/data/user/0/org.chromium.chrome
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    usesStaticLibraries:
      app.vanadium.trichromelibrary version:631208133
    usesOptionalLibraries:
      androidx.window.extensions
    usesLibraryFiles:
      /data/app/~~nblkwv3PQh7_z_fZ__y8Yw==/app.vanadium.trichromelibrary_631208133-ECg2o_IX1ClB00tmW7Jjuw==/base.apk
    timeStamp=2024-04-02 15:30:29
    lastUpdateTime=2024-04-02 15:32:41
    installerPackageName=app.grapheneos.apps
    installerPackageUid=10173
    initiatingPackageName=app.grapheneos.apps
    originatingPackageName=null
    packageSource=2
    appMetadataFilePath=null
    signatures=PackageSignatures{ecf05ba version:3, signatures:[c5600820], past signatures:[]}
    installPermissionsFixed=true
    pkgFlags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA UPDATED_SYSTEM_APP ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION HAS_DOMAIN_URLS PARTIALLY_DIRECT_BOOT_AWARE PRODUCT PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    declared permissions:
      app.vanadium.browser.permission.CHILD_SERVICE: prot=signature
      app.vanadium.browser.permission.READ_WRITE_BOOKMARK_FOLDERS: prot=signature|privileged
      app.vanadium.browser.TOS_ACKED: prot=signature|privileged
      app.vanadium.browser.permission.C2D_MESSAGE: prot=signature
      app.vanadium.browser.permission.DEBUG: prot=signature
    install permissions:
      android.permission.DOWNLOAD_WITHOUT_NOTIFICATION: granted=true
      com.google.android.c2dm.permission.RECEIVE: granted=true
      android.permission.USE_CREDENTIALS: granted=true
      android.permission.MODIFY_AUDIO_SETTINGS: granted=true
      android.permission.MANAGE_ACCOUNTS: granted=true
      android.permission.NFC: granted=true
      android.permission.FOREGROUND_SERVICE: granted=true
      android.permission.RECEIVE_BOOT_COMPLETED: granted=true
      app.vanadium.browser.permission.READ_WRITE_BOOKMARK_FOLDERS: granted=true
      android.permission.BLUETOOTH: granted=true
      android.permission.REORDER_TASKS: granted=true
      android.permission.CREDENTIAL_MANAGER_SET_ALLOWED_PROVIDERS: granted=true
      app.vanadium.browser.TOS_ACKED: granted=true
      android.permission.FOREGROUND_SERVICE_DATA_SYNC: granted=true
      android.permission.ACCESS_NETWORK_STATE: granted=true
      android.permission.RUN_USER_INITIATED_JOBS: granted=true
      android.permission.CREDENTIAL_MANAGER_SET_ORIGIN: granted=true
      android.permission.ACCESS_ADSERVICES_ATTRIBUTION: granted=true
      android.permission.USE_FINGERPRINT: granted=true
      android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK: granted=true
      android.permission.VIBRATE: granted=true
      android.permission.ACCESS_WIFI_STATE: granted=true
      android.permission.USE_BIOMETRIC: granted=true
      android.permission.REQUEST_INSTALL_PACKAGES: granted=false
      com.android.launcher.permission.INSTALL_SHORTCUT: granted=true
      android.permission.QUERY_ALL_PACKAGES: granted=true
      app.vanadium.browser.permission.C2D_MESSAGE: granted=true
      android.permission.WAKE_LOCK: granted=true
      android.permission.CREDENTIAL_MANAGER_QUERY_CANDIDATE_CREDENTIALS: granted=true
    User 0: ceDataInode=1352 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[3002, 3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.ACCESS_FINE_LOCATION: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|AUTO_REVOKED]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_CONNECT: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.INTERNET: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.ACCESS_COARSE_LOCATION: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|AUTO_REVOKED]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.CAMERA: granted=false, flags=[ USER_SET|USER_FIXED|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_ADVERTISE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.GET_ACCOUNTS: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.RECORD_AUDIO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_CONTACTS: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_SCAN: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
      disabledComponents:
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderSmall
        org.chromium.chrome.browser.media.MediaLauncherActivity
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderMedium
        org.chromium.chrome.browser.media.AudioLauncherActivity
        org.chromium.chrome.browser.sharing.shared_clipboard.SharedClipboardShareActivity
      enabledComponents:
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderDino
        org.chromium.chrome.browser.incognito.IncognitoTabLauncher
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderSearch
    User 10: ceDataInode=524787 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[3002, 3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.ACCESS_FINE_LOCATION: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_CONNECT: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.INTERNET: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.ACCESS_COARSE_LOCATION: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.CAMERA: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_ADVERTISE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.GET_ACCOUNTS: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.RECORD_AUDIO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_CONTACTS: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_SCAN: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
      disabledComponents:
        org.chromium.chrome.browser.media.MediaLauncherActivity
        org.chromium.chrome.browser.media.AudioLauncherActivity
        org.chromium.chrome.browser.sharing.shared_clipboard.SharedClipboardShareActivity
      enabledComponents:
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderDino
        org.chromium.chrome.browser.incognito.IncognitoTabLauncher
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderSearch
    User 11: ceDataInode=5153 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[3002, 3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.ACCESS_FINE_LOCATION: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_CONNECT: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.INTERNET: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.ACCESS_COARSE_LOCATION: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.CAMERA: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_ADVERTISE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.GET_ACCOUNTS: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.RECORD_AUDIO: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_CONTACTS: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_SCAN: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
      disabledComponents:
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderSmall
        org.chromium.chrome.browser.media.MediaLauncherActivity
        org.chromium.chrome.browser.printing.PrintShareActivity
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderMedium
        org.chromium.chrome.browser.media.AudioLauncherActivity
        org.chromium.chrome.browser.sharing.shared_clipboard.SharedClipboardShareActivity
      enabledComponents:
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderDino
        org.chromium.chrome.browser.incognito.IncognitoTabLauncher
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderSearch
    User 13: ceDataInode=17560 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      gids=[3002, 3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.ACCESS_FINE_LOCATION: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_CONNECT: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.INTERNET: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.ACCESS_COARSE_LOCATION: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.CAMERA: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_ADVERTISE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.GET_ACCOUNTS: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.RECORD_AUDIO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_CONTACTS: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_SCAN: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
      disabledComponents:
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderDino
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderSmall
        org.chromium.chrome.browser.media.MediaLauncherActivity
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderMedium
        org.chromium.chrome.browser.quickactionsearchwidget.QuickActionSearchWidgetProvider$QuickActionSearchWidgetProviderSearch
        org.chromium.chrome.browser.media.AudioLauncherActivity
        org.chromium.chrome.browser.sharing.shared_clipboard.SharedClipboardShareActivity
      enabledComponents:
        org.chromium.chrome.browser.incognito.IncognitoTabLauncher
    User 17: ceDataInode=441280 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      gids=[3002, 3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.ACCESS_FINE_LOCATION: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_CONNECT: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.INTERNET: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.ACCESS_COARSE_LOCATION: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_IMAGES: granted=false
        android.permission.CAMERA: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_AUDIO: granted=false
        android.permission.READ_MEDIA_VIDEO: granted=false
        android.permission.BLUETOOTH_ADVERTISE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.GET_ACCOUNTS: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.RECORD_AUDIO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_CONTACTS: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_SCAN: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
  Package [com.sony.songpal.mdr] (4b74de):
    appId=10124
    pkg=Package{3eb53c8 com.sony.songpal.mdr}
    codePath=/data/app/~~toYTo2nQJeGHpaPIbXpZ8Q==/com.sony.songpal.mdr-tLFRIwOOKOfGnYTrQ-1TSg==
    resourcePath=/data/app/~~toYTo2nQJeGHpaPIbXpZ8Q==/com.sony.songpal.mdr-tLFRIwOOKOfGnYTrQ-1TSg==
    legacyNativeLibraryDir=/data/app/~~toYTo2nQJeGHpaPIbXpZ8Q==/com.sony.songpal.mdr-tLFRIwOOKOfGnYTrQ-1TSg==/lib
    extractNativeLibs=true
    primaryCpuAbi=arm64-v8a
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=10020050 minSdk=28 targetSdk=34
    minExtensionVersions=[]
    versionName=10.2.0
    usesNonSdkApi=false
    splits=[base]
    apkSigningVersion=2
    flags=[ HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP LARGE_HEAP ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PARTIALLY_DIRECT_BOOT_AWARE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    queriesIntents=[Intent { act=android.intent.action.VIEW cat=[android.intent.category.BROWSABLE] dat=https:/... }, Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] }, Intent { act=android.intent.action.TTS_SERVICE }]
    dataDir=/data/user/0/com.sony.songpal.mdr
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    usesOptionalLibraries:
      org.apache.http.legacy
    usesLibraryFiles:
      /system/framework/org.apache.http.legacy.jar
    timeStamp=2023-11-08 08:06:00
    lastUpdateTime=2023-11-08 08:06:16
    installerPackageName=com.aurora.store
    installerPackageUid=-1
    initiatingPackageName=com.aurora.store
    originatingPackageName=null
    packageSource=2
    appMetadataFilePath=null
    signatures=PackageSignatures{369cc61 version:2, signatures:[3d69bbc5], past signatures:[]}
    installPermissionsFixed=true
    pkgFlags=[ HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP LARGE_HEAP ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PARTIALLY_DIRECT_BOOT_AWARE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    declared permissions:
      com.sony.songpal.mdr.permission.C2D_MESSAGE: prot=signature
      com.sony.songpal.mdr.application.permission.mdr_info: prot=normal
      com.sony.songpal.mdr.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION: prot=signature
    install permissions:
      com.sony.songpal.mdr.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION: granted=true
      com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE: granted=true
      com.google.android.c2dm.permission.RECEIVE: granted=true
      android.permission.REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND: granted=true
      android.permission.FOREGROUND_SERVICE: granted=true
      android.permission.BLUETOOTH: granted=true
      android.permission.BLUETOOTH_ADMIN: granted=true
      com.sony.songpal.mdr.permission.C2D_MESSAGE: granted=true
      android.permission.ACCESS_NETWORK_STATE: granted=true
      android.permission.VIBRATE: granted=true
      android.permission.FOREGROUND_SERVICE_CONNECTED_DEVICE: granted=true
      com.google.android.gms.permission.AD_ID: granted=true
      android.permission.WAKE_LOCK: granted=true
    User 0: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2023-02-21 12:09:40
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[3002, 3001]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.ACCESS_FINE_LOCATION: granted=false
        android.permission.OTHER_SENSORS: granted=false
        android.permission.BLUETOOTH_CONNECT: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ REVOKE_WHEN_REQUESTED|APPLY_RESTRICTION]
        android.permission.ACCESS_COARSE_LOCATION: granted=false
        android.permission.CAMERA: granted=false
        android.permission.ACCESS_BACKGROUND_LOCATION: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.BLUETOOTH_SCAN: granted=false
    User 10: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[3002, 3001]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.ACCESS_FINE_LOCATION: granted=false
        android.permission.OTHER_SENSORS: granted=false
        android.permission.BLUETOOTH_CONNECT: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ REVOKE_WHEN_REQUESTED|APPLY_RESTRICTION]
        android.permission.ACCESS_COARSE_LOCATION: granted=false
        android.permission.CAMERA: granted=false
        android.permission.ACCESS_BACKGROUND_LOCATION: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.BLUETOOTH_SCAN: granted=false
    User 11: ceDataInode=1055516 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2023-02-21 12:09:42
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[3002, 3003, 3001]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.ACCESS_FINE_LOCATION: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.BLUETOOTH_CONNECT: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.INTERNET: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ REVOKE_WHEN_REQUESTED|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
        android.permission.ACCESS_COARSE_LOCATION: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.CAMERA: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.ACCESS_BACKGROUND_LOCATION: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
        android.permission.BLUETOOTH_SCAN: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
      enabledComponents:
        com.google.android.play.core.common.PlayCoreDialogWrapperActivity
    User 13: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      gids=[3002, 3001]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.ACCESS_FINE_LOCATION: granted=false
        android.permission.OTHER_SENSORS: granted=false
        android.permission.BLUETOOTH_CONNECT: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ REVOKE_WHEN_REQUESTED|APPLY_RESTRICTION]
        android.permission.ACCESS_COARSE_LOCATION: granted=false
        android.permission.CAMERA: granted=false
        android.permission.ACCESS_BACKGROUND_LOCATION: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.BLUETOOTH_SCAN: granted=false
    User 17: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      gids=[3002, 3001]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.ACCESS_FINE_LOCATION: granted=false
        android.permission.OTHER_SENSORS: granted=false
        android.permission.BLUETOOTH_CONNECT: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.ACCESS_COARSE_LOCATION: granted=false
        android.permission.CAMERA: granted=false
        android.permission.ACCESS_BACKGROUND_LOCATION: granted=false
        android.permission.BLUETOOTH_SCAN: granted=false
  Package [com.android.adservices.api] (f7096bf):
    appId=10228
    pkg=Package{6954447 com.android.adservices.api}
    codePath=/apex/com.android.adservices/priv-app/AdServicesApk@UP1A.231105.001
    resourcePath=/apex/com.android.adservices/priv-app/AdServicesApk@UP1A.231105.001
    legacyNativeLibraryDir=/apex/com.android.adservices/priv-app/AdServicesApk@UP1A.231105.001/lib
    extractNativeLibs=false
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=34 minSdk=33 targetSdk=34
    minExtensionVersions=[]
    versionName=14
    usesNonSdkApi=true
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PARTIALLY_DIRECT_BOOT_AWARE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=true
    dataDir=/data/user/0/com.android.adservices.api
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=1970-01-01 01:00:00
    lastUpdateTime=1970-01-01 01:00:00
    installerPackageName=null
    installerPackageUid=-1
    initiatingPackageName=null
    originatingPackageName=null
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{e45e474 version:3, signatures:[4594e6f4], past signatures:[]}
    installPermissionsFixed=false
    pkgFlags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PARTIALLY_DIRECT_BOOT_AWARE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=com.android.adservices
    declared permissions:
      android.permission.ACCESS_ADSERVICES_TOPICS: prot=normal
      android.permission.ACCESS_ADSERVICES_ATTRIBUTION: prot=normal
      android.permission.ACCESS_ADSERVICES_CUSTOM_AUDIENCE: prot=normal
      android.permission.ACCESS_ADSERVICES_AD_ID: prot=normal
      android.permission.ACCESS_PRIVILEGED_AD_ID: prot=signature
      android.permission.ACCESS_PRIVILEGED_APP_SET_ID: prot=signature
      android.permission.MODIFY_ADSERVICES_STATE: prot=signature|configurator
      android.permission.ACCESS_ADSERVICES_STATE: prot=signature|configurator
      android.permission.ACCESS_ADSERVICES_MANAGER: prot=signature
      com.android.adservices.api.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION: prot=signature
    install permissions:
      android.permission.ACCESS_ADSERVICES_MANAGER: granted=true
      android.permission.RECEIVE_BOOT_COMPLETED: granted=true
      android.permission.PACKAGE_USAGE_STATS: granted=true
      android.permission.ACCESS_PRIVILEGED_APP_SET_ID: granted=true
      android.permission.ACCESS_NETWORK_STATE: granted=true
      com.android.adservices.api.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION: granted=true
      android.permission.ACCESS_PRIVILEGED_AD_ID: granted=true
      android.permission.QUERY_ALL_PACKAGES: granted=true
      android.permission.READ_DEVICE_CONFIG: granted=true
    User 0: ceDataInode=812242 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ GRANTED_BY_DEFAULT]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.INTERNET: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 10: ceDataInode=276402 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ GRANTED_BY_DEFAULT]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.INTERNET: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 11: ceDataInode=800382 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ GRANTED_BY_DEFAULT]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.INTERNET: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 13: ceDataInode=880303 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      gids=[3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ GRANTED_BY_DEFAULT]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.INTERNET: granted=true
    User 17: ceDataInode=0 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      gids=[3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ GRANTED_BY_DEFAULT]
        android.permission.OTHER_SENSORS: granted=true
        android.permission.INTERNET: granted=true
  Package [io.metamask] (798918c):
    appId=10186
    pkg=Package{35c9212 io.metamask}
    codePath=/data/app/~~EVOKCUwVRGY2GPSrp8WjJw==/io.metamask-5bC0b4Uxe3j93qjigZLORA==
    resourcePath=/data/app/~~EVOKCUwVRGY2GPSrp8WjJw==/io.metamask-5bC0b4Uxe3j93qjigZLORA==
    legacyNativeLibraryDir=/data/app/~~EVOKCUwVRGY2GPSrp8WjJw==/io.metamask-5bC0b4Uxe3j93qjigZLORA==/lib
    extractNativeLibs=true
    primaryCpuAbi=arm64-v8a
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=790 minSdk=19 targetSdk=29
    minExtensionVersions=[]
    versionName=3.6.0
    usesNonSdkApi=false
    splits=[base]
    apkSigningVersion=2
    flags=[ HAS_CODE ALLOW_CLEAR_USER_DATA LARGE_HEAP ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE HAS_DOMAIN_URLS PARTIALLY_DIRECT_BOOT_AWARE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    dataDir=/data/user/0/io.metamask
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    usesLibraries:
      android.test.base
    usesOptionalLibraries:
      android.test.mock
      org.apache.http.legacy
      android.test.runner
    usesLibraryFiles:
      /system/framework/android.test.base.jar
      /system/framework/android.test.mock.jar
      /system/framework/org.apache.http.legacy.jar
      /system/framework/android.test.runner.jar
    timeStamp=2021-11-14 03:43:48
    lastUpdateTime=2021-11-14 03:43:48
    installerPackageName=com.android.packageinstaller
    installerPackageUid=-1
    initiatingPackageName=com.android.packageinstaller
    originatingPackageName=org.chromium.chrome
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{ed7dde3 version:2, signatures:[9ca933a7], past signatures:[]}
    installPermissionsFixed=true
    pkgFlags=[ HAS_CODE ALLOW_CLEAR_USER_DATA LARGE_HEAP ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE HAS_DOMAIN_URLS PARTIALLY_DIRECT_BOOT_AWARE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    install permissions:
      com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE: granted=true
      com.google.android.c2dm.permission.RECEIVE: granted=true
      android.permission.SYSTEM_ALERT_WINDOW: granted=false
      com.android.vending.CHECK_LICENSE: granted=true
      android.permission.ACCESS_NETWORK_STATE: granted=true
      android.permission.USE_FINGERPRINT: granted=true
      android.permission.ACCESS_WIFI_STATE: granted=true
      android.permission.USE_BIOMETRIC: granted=true
      android.permission.WAKE_LOCK: granted=true
    User 0: ceDataInode=148231 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=4
      firstInstallTime=2021-11-14 03:43:48
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false, flags=[ REVOKE_WHEN_REQUESTED|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.INTERNET: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ REVOKE_WHEN_REQUESTED|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ REVOKE_WHEN_REQUESTED|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
        android.permission.CAMERA: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ REVOKE_WHEN_REQUESTED|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ REVOKE_WHEN_REQUESTED|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
    User 10: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2021-11-14 03:43:48
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.OTHER_SENSORS: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ REVOKE_WHEN_REQUESTED|APPLY_RESTRICTION]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.CAMERA: granted=false
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ APPLY_RESTRICTION]
    User 11: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2021-11-14 03:43:48
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.OTHER_SENSORS: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ REVOKE_WHEN_REQUESTED|APPLY_RESTRICTION]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.CAMERA: granted=false
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ APPLY_RESTRICTION]
    User 13: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2021-11-14 03:43:48
      uninstallReason=0
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.OTHER_SENSORS: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ REVOKE_WHEN_REQUESTED|APPLY_RESTRICTION]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.CAMERA: granted=false
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ REVOKE_WHEN_REQUESTED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ APPLY_RESTRICTION]
    User 17: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2021-11-14 03:43:48
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false, flags=[ REVOKE_WHEN_REQUESTED|APPLY_RESTRICTION]
        android.permission.OTHER_SENSORS: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ REVOKE_WHEN_REQUESTED|APPLY_RESTRICTION]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ REVOKE_WHEN_REQUESTED|APPLY_RESTRICTION]
        android.permission.CAMERA: granted=false
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ REVOKE_WHEN_REQUESTED|APPLY_RESTRICTION]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ REVOKE_WHEN_REQUESTED|APPLY_RESTRICTION]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ APPLY_RESTRICTION]
  Package [de.blinkt.openvpn] (696d0d5):
    appId=10233
    pkg=Package{586a699 de.blinkt.openvpn}
    codePath=/data/app/~~UmgbunhC6B0DZ0Wmg8T8hw==/de.blinkt.openvpn-LUpGBzKOoMuGr3bcZ_FUOQ==
    resourcePath=/data/app/~~UmgbunhC6B0DZ0Wmg8T8hw==/de.blinkt.openvpn-LUpGBzKOoMuGr3bcZ_FUOQ==
    legacyNativeLibraryDir=/data/app/~~UmgbunhC6B0DZ0Wmg8T8hw==/de.blinkt.openvpn-LUpGBzKOoMuGr3bcZ_FUOQ==/lib
    extractNativeLibs=true
    primaryCpuAbi=arm64-v8a
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=189 minSdk=16 targetSdk=31
    minExtensionVersions=[]
    versionName=0.7.34
    usesNonSdkApi=false
    splits=[base]
    apkSigningVersion=3
    flags=[ HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    dataDir=/data/user/0/de.blinkt.openvpn
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=2022-05-06 23:28:23
    lastUpdateTime=2022-05-06 23:28:23
    installerPackageName=com.android.packageinstaller
    installerPackageUid=-1
    initiatingPackageName=com.android.packageinstaller
    originatingPackageName=org.fdroid.fdroid
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{46dbd5e version:3, signatures:[1de77dfe], past signatures:[]}
    installPermissionsFixed=true
    pkgFlags=[ HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    install permissions:
      android.permission.FOREGROUND_SERVICE: granted=true
      android.permission.RECEIVE_BOOT_COMPLETED: granted=true
      android.permission.ACCESS_NETWORK_STATE: granted=true
      android.permission.QUERY_ALL_PACKAGES: granted=true
    User 0: ceDataInode=545379 installed=true hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=false enabled=0 instant=false virtual=false
      installReason=4
      firstInstallTime=2022-05-02 23:18:53
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[3003]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.INTERNET: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRICTION_INSTALLER_EXEMPT]
    User 10: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2022-05-02 23:18:53
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false
        android.permission.OTHER_SENSORS: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ APPLY_RESTRICTION]
    User 11: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2022-05-02 23:18:53
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false
        android.permission.OTHER_SENSORS: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.READ_MEDIA_IMAGES: granted=false
        android.permission.READ_MEDIA_AUDIO: granted=false
        android.permission.READ_MEDIA_VIDEO: granted=false
    User 13: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2022-05-02 23:18:53
      uninstallReason=0
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.OTHER_SENSORS: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.READ_MEDIA_IMAGES: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.READ_MEDIA_AUDIO: granted=false, flags=[ APPLY_RESTRICTION]
        android.permission.READ_MEDIA_VIDEO: granted=false, flags=[ APPLY_RESTRICTION]
    User 17: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2022-05-02 23:18:53
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=false
        android.permission.OTHER_SENSORS: granted=false
        android.permission.INTERNET: granted=false
        android.permission.READ_EXTERNAL_STORAGE: granted=false
        android.permission.READ_MEDIA_IMAGES: granted=false
        android.permission.READ_MEDIA_AUDIO: granted=false
        android.permission.READ_MEDIA_VIDEO: granted=false
  Package [com.android.internal.display.cutout.emulation.double] (e050bf4):
    appId=10019
    pkg=Package{a454e0c com.android.internal.display.cutout.emulation.double}
    codePath=/product/overlay/DisplayCutoutEmulationDouble
    resourcePath=/product/overlay/DisplayCutoutEmulationDouble
    legacyNativeLibraryDir=/product/overlay/DisplayCutoutEmulationDouble/lib
    extractNativeLibs=true
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=1 minSdk=34 targetSdk=34
    minExtensionVersions=[]
    versionName=1.0
    usesNonSdkApi=false
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRODUCT PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    dataDir=/data/user/0/com.android.internal.display.cutout.emulation.double
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=2009-01-01 00:00:00
    lastUpdateTime=2009-01-01 00:00:00
    installerPackageName=null
    installerPackageUid=-1
    initiatingPackageName=null
    originatingPackageName=null
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{6921355 version:3, signatures:[4594e6f4], past signatures:[]}
    installPermissionsFixed=false
    pkgFlags=[ SYSTEM ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRODUCT PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    overlayTarget=android
    overlayCategory=com.android.internal.display_cutout_emulation
    User 0: ceDataInode=1355 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 10: ceDataInode=542695 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 11: ceDataInode=5159 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 13: ceDataInode=17940 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 17: ceDataInode=138291 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
  Package [com.android.providers.telephony] (e3c4b08):
    appId=1001
    sharedUser=SharedUserSetting{b9600ea android.uid.phone/1001}
    pkg=Package{b31265b com.android.providers.telephony}
    codePath=/system/priv-app/TelephonyProvider
    resourcePath=/system/priv-app/TelephonyProvider
    legacyNativeLibraryDir=/system/priv-app/TelephonyProvider/lib
    extractNativeLibs=true
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=34 minSdk=34 targetSdk=34
    minExtensionVersions=[]
    versionName=14
    usesNonSdkApi=true
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM HAS_CODE ALLOW_BACKUP KILL_AFTER_RESTORE RESTORE_ANY_VERSION ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE BACKUP_IN_FOREGROUND DEFAULT_TO_DEVICE_PROTECTED_STORAGE DIRECT_BOOT_AWARE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=true
    dataDir=/data/user_de/0/com.android.providers.telephony
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=2009-01-01 00:00:00
    lastUpdateTime=2009-01-01 00:00:00
    installerPackageName=null
    installerPackageUid=-1
    initiatingPackageName=null
    originatingPackageName=null
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{2ff3ef8 version:3, signatures:[2297f32d], past signatures:[]}
    installPermissionsFixed=false
    pkgFlags=[ SYSTEM HAS_CODE ALLOW_BACKUP KILL_AFTER_RESTORE RESTORE_ANY_VERSION ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE BACKUP_IN_FOREGROUND DEFAULT_TO_DEVICE_PROTECTED_STORAGE DIRECT_BOOT_AWARE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    declared permissions:
      android.permission.ACCESS_TELEPHONY_SIMINFO_DB: prot=signature
    User 0: ceDataInode=1358 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
    User 10: ceDataInode=517916 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
    User 11: ceDataInode=5165 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
    User 13: ceDataInode=18044 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
    User 17: ceDataInode=22975 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
  Package [com.android.dynsystem] (3f0b4a):
    appId=1000
    sharedUser=SharedUserSetting{221dfdb android.uid.system/1000}
    pkg=Package{35e1a36 com.android.dynsystem}
    codePath=/system/priv-app/DynamicSystemInstallationService
    resourcePath=/system/priv-app/DynamicSystemInstallationService
    legacyNativeLibraryDir=/system/priv-app/DynamicSystemInstallationService/lib
    extractNativeLibs=true
    primaryCpuAbi=arm64-v8a
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=34 minSdk=34 targetSdk=34
    minExtensionVersions=[]
    versionName=14
    usesNonSdkApi=true
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    dataDir=/data/user/0/com.android.dynsystem
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=2009-01-01 00:00:00
    lastUpdateTime=2009-01-01 00:00:00
    installerPackageName=null
    installerPackageUid=-1
    initiatingPackageName=null
    originatingPackageName=null
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{6d1cd37 version:3, signatures:[2297f32d], past signatures:[]}
    installPermissionsFixed=false
    pkgFlags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    User 0: ceDataInode=1361 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
    User 10: ceDataInode=480595 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
    User 11: ceDataInode=5171 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
    User 13: ceDataInode=18096 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
    User 17: ceDataInode=169350 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
  Package [app.grapheneos.gmscompat.config] (9033a78):
    appId=10195
    pkg=Package{560f360 app.grapheneos.gmscompat.config}
    codePath=/data/app/~~5x60aJP9A2ONZSd25PteZg==/app.grapheneos.gmscompat.config-Q-iPFMgJS1pR48i5Assrmw==
    resourcePath=/data/app/~~5x60aJP9A2ONZSd25PteZg==/app.grapheneos.gmscompat.config-Q-iPFMgJS1pR48i5Assrmw==
    legacyNativeLibraryDir=/data/app/~~5x60aJP9A2ONZSd25PteZg==/app.grapheneos.gmscompat.config-Q-iPFMgJS1pR48i5Assrmw==/lib
    extractNativeLibs=false
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=101 minSdk=32 targetSdk=34
    minExtensionVersions=[]
    versionName=101
    usesNonSdkApi=false
    splits=[base]
    apkSigningVersion=2
    flags=[ SYSTEM ALLOW_CLEAR_USER_DATA UPDATED_SYSTEM_APP ALLOW_BACKUP ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    dataDir=/data/user/0/app.grapheneos.gmscompat.config
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=2024-04-03 17:38:40
    lastUpdateTime=2024-04-03 17:38:40
    installerPackageName=app.grapheneos.apps
    installerPackageUid=1010173
    initiatingPackageName=app.grapheneos.apps
    originatingPackageName=null
    packageSource=2
    appMetadataFilePath=null
    signatures=PackageSignatures{fe9a3c2 version:2, signatures:[e429b2ce], past signatures:[]}
    installPermissionsFixed=true
    pkgFlags=[ SYSTEM ALLOW_CLEAR_USER_DATA UPDATED_SYSTEM_APP ALLOW_BACKUP ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    User 0: ceDataInode=812245 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 10: ceDataInode=276222 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2023-01-13 10:14:12
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 11: ceDataInode=800757 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2022-11-18 20:30:49
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 13: ceDataInode=902162 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
    User 17: ceDataInode=0 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true
  Package [com.android.healthconnect.controller] (300a551):
    appId=10174
    pkg=Package{bf6f510 com.android.healthconnect.controller}
    codePath=/apex/com.android.healthfitness/priv-app/HealthConnectController@UP1A.231105.001
    resourcePath=/apex/com.android.healthfitness/priv-app/HealthConnectController@UP1A.231105.001
    legacyNativeLibraryDir=/apex/com.android.healthfitness/priv-app/HealthConnectController@UP1A.231105.001/lib
    extractNativeLibs=false
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=34 minSdk=34 targetSdk=34
    minExtensionVersions=[]
    versionName=14
    usesNonSdkApi=true
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    queriesIntents=[Intent { act=android.intent.action.VIEW_PERMISSION_USAGE cat=[android.intent.category.HEALTH_PERMISSIONS] }]
    dataDir=/data/user/0/com.android.healthconnect.controller
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    usesOptionalLibraries:
      androidx.window.extensions
      androidx.window.sidecar
      org.apache.http.legacy
    usesLibraryFiles:
      /system/framework/org.apache.http.legacy.jar
    timeStamp=1970-01-01 01:00:00
    lastUpdateTime=1970-01-01 01:00:00
    installerPackageName=null
    installerPackageUid=-1
    initiatingPackageName=null
    originatingPackageName=null
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{1316809 version:3, signatures:[220bfb44], past signatures:[]}
    installPermissionsFixed=false
    pkgFlags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=com.android.healthfitness
    declared permissions:
      android.permission.health.READ_ACTIVE_CALORIES_BURNED: prot=dangerous
      android.permission.health.READ_DISTANCE: prot=dangerous
      android.permission.health.READ_ELEVATION_GAINED: prot=dangerous
      android.permission.health.READ_EXERCISE: prot=dangerous
      android.permission.health.READ_EXERCISE_ROUTE: prot=signature
      android.permission.health.READ_FLOORS_CLIMBED: prot=dangerous
      android.permission.health.READ_STEPS: prot=dangerous
      android.permission.health.READ_TOTAL_CALORIES_BURNED: prot=dangerous
      android.permission.health.READ_VO2_MAX: prot=dangerous
      android.permission.health.READ_WHEELCHAIR_PUSHES: prot=dangerous
      android.permission.health.READ_POWER: prot=dangerous
      android.permission.health.READ_SPEED: prot=dangerous
      android.permission.health.READ_BASAL_METABOLIC_RATE: prot=dangerous
      android.permission.health.READ_BODY_FAT: prot=dangerous
      android.permission.health.READ_BODY_WATER_MASS: prot=dangerous
      android.permission.health.READ_BONE_MASS: prot=dangerous
      android.permission.health.READ_HEIGHT: prot=dangerous
      android.permission.health.READ_LEAN_BODY_MASS: prot=dangerous
      android.permission.health.READ_WEIGHT: prot=dangerous
      android.permission.health.READ_CERVICAL_MUCUS: prot=dangerous
      android.permission.health.READ_INTERMENSTRUAL_BLEEDING: prot=dangerous
      android.permission.health.READ_MENSTRUATION: prot=dangerous
      android.permission.health.READ_OVULATION_TEST: prot=dangerous
      android.permission.health.READ_SEXUAL_ACTIVITY: prot=dangerous
      android.permission.health.READ_HYDRATION: prot=dangerous
      android.permission.health.READ_NUTRITION: prot=dangerous
      android.permission.health.READ_SLEEP: prot=dangerous
      android.permission.health.READ_BASAL_BODY_TEMPERATURE: prot=dangerous
      android.permission.health.READ_BLOOD_GLUCOSE: prot=dangerous
      android.permission.health.READ_BLOOD_PRESSURE: prot=dangerous
      android.permission.health.READ_BODY_TEMPERATURE: prot=dangerous
      android.permission.health.READ_HEART_RATE: prot=dangerous
      android.permission.health.READ_HEART_RATE_VARIABILITY: prot=dangerous
      android.permission.health.READ_OXYGEN_SATURATION: prot=dangerous
      android.permission.health.READ_RESPIRATORY_RATE: prot=dangerous
      android.permission.health.READ_RESTING_HEART_RATE: prot=dangerous
      android.permission.health.WRITE_ACTIVE_CALORIES_BURNED: prot=dangerous
      android.permission.health.WRITE_DISTANCE: prot=dangerous
      android.permission.health.WRITE_ELEVATION_GAINED: prot=dangerous
      android.permission.health.WRITE_EXERCISE: prot=dangerous
      android.permission.health.WRITE_EXERCISE_ROUTE: prot=dangerous
      android.permission.health.WRITE_FLOORS_CLIMBED: prot=dangerous
      android.permission.health.WRITE_STEPS: prot=dangerous
      android.permission.health.WRITE_TOTAL_CALORIES_BURNED: prot=dangerous
      android.permission.health.WRITE_VO2_MAX: prot=dangerous
      android.permission.health.WRITE_WHEELCHAIR_PUSHES: prot=dangerous
      android.permission.health.WRITE_POWER: prot=dangerous
      android.permission.health.WRITE_SPEED: prot=dangerous
      android.permission.health.WRITE_BASAL_METABOLIC_RATE: prot=dangerous
      android.permission.health.WRITE_BODY_FAT: prot=dangerous
      android.permission.health.WRITE_BODY_WATER_MASS: prot=dangerous
      android.permission.health.WRITE_BONE_MASS: prot=dangerous
      android.permission.health.WRITE_HEIGHT: prot=dangerous
      android.permission.health.WRITE_LEAN_BODY_MASS: prot=dangerous
      android.permission.health.WRITE_WEIGHT: prot=dangerous
      android.permission.health.WRITE_CERVICAL_MUCUS: prot=dangerous
      android.permission.health.WRITE_INTERMENSTRUAL_BLEEDING: prot=dangerous
      android.permission.health.WRITE_MENSTRUATION: prot=dangerous
      android.permission.health.WRITE_OVULATION_TEST: prot=dangerous
      android.permission.health.WRITE_SEXUAL_ACTIVITY: prot=dangerous
      android.permission.health.WRITE_HYDRATION: prot=dangerous
      android.permission.health.WRITE_NUTRITION: prot=dangerous
      android.permission.health.WRITE_SLEEP: prot=dangerous
      android.permission.health.WRITE_BASAL_BODY_TEMPERATURE: prot=dangerous
      android.permission.health.WRITE_BLOOD_GLUCOSE: prot=dangerous
      android.permission.health.WRITE_BLOOD_PRESSURE: prot=dangerous
      android.permission.health.WRITE_BODY_TEMPERATURE: prot=dangerous
      android.permission.health.WRITE_HEART_RATE: prot=dangerous
      android.permission.health.WRITE_HEART_RATE_VARIABILITY: prot=dangerous
      android.permission.health.WRITE_OXYGEN_SATURATION: prot=dangerous
      android.permission.health.WRITE_RESPIRATORY_RATE: prot=dangerous
      android.permission.health.WRITE_RESTING_HEART_RATE: prot=dangerous
      android.permission.MANAGE_HEALTH_PERMISSIONS: prot=signature
      android.permission.MANAGE_HEALTH_DATA: prot=signature|privileged
      com.android.healthconnect.controller.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION: prot=signature
    install permissions:
      android.permission.LAUNCH_MULTI_PANE_SETTINGS_DEEP_LINK: granted=true
      android.permission.health.READ_EXERCISE_ROUTE: granted=true
      android.permission.MANAGE_HEALTH_DATA: granted=true
      android.permission.SEND_SAFETY_CENTER_UPDATE: granted=true
      com.android.healthconnect.controller.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION: granted=true
      android.permission.MANAGE_HEALTH_PERMISSIONS: granted=true
      android.permission.START_VIEW_PERMISSION_USAGE: granted=true
      android.permission.READ_DEVICE_CONFIG: granted=true
    User 0: ceDataInode=1222955 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.READ_PHONE_STATE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|RESTRICTION_UPGRADE_EXEMPT]
    User 10: ceDataInode=1409291 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.READ_PHONE_STATE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|RESTRICTION_UPGRADE_EXEMPT]
    User 11: ceDataInode=1194863 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.READ_PHONE_STATE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|RESTRICTION_UPGRADE_EXEMPT]
    User 13: ceDataInode=0 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true
        android.permission.READ_EXTERNAL_STORAGE: granted=false
        android.permission.READ_PHONE_STATE: granted=false
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false
    User 17: ceDataInode=0 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true
        android.permission.READ_EXTERNAL_STORAGE: granted=false
        android.permission.READ_PHONE_STATE: granted=false
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false
  Package [com.android.providers.calendar] (f2ab7dd):
    appId=10035
    sharedUser=SharedUserSetting{74b41b6 android.uid.calendar/10035}
    pkg=Package{1672c2f com.android.providers.calendar}
    codePath=/system/priv-app/CalendarProvider
    resourcePath=/system/priv-app/CalendarProvider
    legacyNativeLibraryDir=/system/priv-app/CalendarProvider/lib
    extractNativeLibs=true
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=34 minSdk=34 targetSdk=34
    minExtensionVersions=[]
    versionName=14
    usesNonSdkApi=true
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=true
    dataDir=/data/user/0/com.android.providers.calendar
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=2009-01-01 00:00:00
    lastUpdateTime=2009-01-01 00:00:00
    installerPackageName=null
    installerPackageUid=-1
    initiatingPackageName=null
    originatingPackageName=null
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{3be523c version:3, signatures:[4594e6f4], past signatures:[]}
    installPermissionsFixed=false
    pkgFlags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    User 0: ceDataInode=1364 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
    User 10: ceDataInode=480606 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
    User 11: ceDataInode=5177 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
    User 13: ceDataInode=18075 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
    User 17: ceDataInode=425093 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
  Package [com.android.providers.media] (3e62cbc):
    appId=10025
    sharedUser=SharedUserSetting{1d49eb7 android.media/10025}
    pkg=Package{c5be91a com.android.providers.media}
    codePath=/system/priv-app/MediaProviderLegacy
    resourcePath=/system/priv-app/MediaProviderLegacy
    legacyNativeLibraryDir=/system/priv-app/MediaProviderLegacy/lib
    extractNativeLibs=true
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=1024 minSdk=34 targetSdk=34
    minExtensionVersions=[]
    versionName=14
    usesNonSdkApi=true
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=true
    dataDir=/data/user/0/com.android.providers.media
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=2009-01-01 00:00:00
    lastUpdateTime=2009-01-01 00:00:00
    installerPackageName=null
    installerPackageUid=-1
    initiatingPackageName=null
    originatingPackageName=null
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{8445c4b version:3, signatures:[1e4e765a], past signatures:[]}
    installPermissionsFixed=false
    pkgFlags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    declared permissions:
      com.android.providers.media.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION: prot=signature
    User 0: ceDataInode=1367 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
    User 10: ceDataInode=480615 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
    User 11: ceDataInode=5183 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
    User 13: ceDataInode=17788 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
    User 17: ceDataInode=426957 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
  Package [com.stevesoltys.seedvault] (86d8624):
    appId=10023
    pkg=Package{4e10f41 com.stevesoltys.seedvault}
    codePath=/system/priv-app/Seedvault
    resourcePath=/system/priv-app/Seedvault
    legacyNativeLibraryDir=/system/priv-app/Seedvault/lib
    extractNativeLibs=true
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=34030030 minSdk=34 targetSdk=34
    minExtensionVersions=[]
    versionName=14-3.3
    usesNonSdkApi=true
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PARTIALLY_DIRECT_BOOT_AWARE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    dataDir=/data/user/0/com.stevesoltys.seedvault
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=2009-01-01 00:00:00
    lastUpdateTime=2009-01-01 00:00:00
    installerPackageName=null
    installerPackageUid=-1
    initiatingPackageName=null
    originatingPackageName=null
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{3bf7ce6 version:3, signatures:[2297f32d], past signatures:[]}
    installPermissionsFixed=false
    pkgFlags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PARTIALLY_DIRECT_BOOT_AWARE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    declared permissions:
      com.stevesoltys.seedvault.OPEN_SETTINGS: prot=signature|privileged
      com.stevesoltys.seedvault.RESTORE_BACKUP: prot=signature|privileged
      com.stevesoltys.seedvault.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION: prot=signature
    install permissions:
      android.permission.MANAGE_EXTERNAL_STORAGE: granted=true
      android.permission.INSTALL_PACKAGES: granted=true
      android.permission.FOREGROUND_SERVICE: granted=true
      android.permission.RECEIVE_BOOT_COMPLETED: granted=true
      com.stevesoltys.seedvault.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION: granted=true
      android.permission.MANAGE_USB: granted=true
      android.permission.INTERACT_ACROSS_USERS_FULL: granted=true
      android.permission.WRITE_SECURE_SETTINGS: granted=true
      android.permission.FOREGROUND_SERVICE_DATA_SYNC: granted=true
      android.permission.MANAGE_USERS: granted=true
      android.permission.ACCESS_NETWORK_STATE: granted=true
      android.permission.BACKUP: granted=true
      android.permission.READ_LOGS: granted=true
      android.permission.REQUEST_DELETE_PACKAGES: granted=true
      android.permission.MANAGE_DOCUMENTS: granted=true
      android.permission.USE_BIOMETRIC: granted=true
      android.permission.QUERY_ALL_PACKAGES: granted=true
    User 0: ceDataInode=1370 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[1007]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.ACCESS_MEDIA_LOCATION: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT]
    User 10: ceDataInode=539484 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[1007]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.ACCESS_MEDIA_LOCATION: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT]
    User 11: ceDataInode=5189 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      gids=[1007]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.ACCESS_MEDIA_LOCATION: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT]
      enabledComponents:
        com.stevesoltys.seedvault.settings.SettingsActivity
    User 13: ceDataInode=8640 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      gids=[1007]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET|USER_SENSITIVE_WHEN_GRANTED]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.ACCESS_MEDIA_LOCATION: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT]
      enabledComponents:
        com.stevesoltys.seedvault.settings.SettingsActivity
    User 17: ceDataInode=406775 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      gids=[1007]
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ USER_SET]
        android.permission.READ_MEDIA_VISUAL_USER_SELECTED: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|USER_SENSITIVE_WHEN_GRANTED]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.ACCESS_MEDIA_LOCATION: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|USER_SENSITIVE_WHEN_GRANTED]
  Package [com.anysoftkeyboard.languagepack.russian2] (959458d):
    appId=10241
    pkg=Package{414acd4 com.anysoftkeyboard.languagepack.russian2}
    codePath=/data/app/~~hp5Dm8znlGlvYnyoC4gwUg==/com.anysoftkeyboard.languagepack.russian2-O9jYMDp-aOP-YqlOsJ4S2A==
    resourcePath=/data/app/~~hp5Dm8znlGlvYnyoC4gwUg==/com.anysoftkeyboard.languagepack.russian2-O9jYMDp-aOP-YqlOsJ4S2A==
    legacyNativeLibraryDir=/data/app/~~hp5Dm8znlGlvYnyoC4gwUg==/com.anysoftkeyboard.languagepack.russian2-O9jYMDp-aOP-YqlOsJ4S2A==/lib
    extractNativeLibs=true
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=2908 minSdk=9 targetSdk=29
    minExtensionVersions=[]
    versionName=4.0.1396
    usesNonSdkApi=false
    splits=[base]
    apkSigningVersion=3
    flags=[ HAS_CODE ALLOW_CLEAR_USER_DATA ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    dataDir=/data/user/0/com.anysoftkeyboard.languagepack.russian2
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    usesLibraries:
      android.test.base
    usesLibraryFiles:
      /system/framework/android.test.base.jar
    timeStamp=2022-05-29 00:20:26
    lastUpdateTime=2022-05-29 00:20:26
    installerPackageName=com.android.packageinstaller
    installerPackageUid=-1
    initiatingPackageName=com.android.packageinstaller
    originatingPackageName=org.fdroid.fdroid
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{96e5e7d version:3, signatures:[9c4a9cf8], past signatures:[]}
    installPermissionsFixed=true
    pkgFlags=[ HAS_CODE ALLOW_CLEAR_USER_DATA ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=null
    User 0: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2022-05-29 00:20:26
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.OTHER_SENSORS: granted=false
    User 10: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2022-05-29 00:20:26
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.OTHER_SENSORS: granted=false
    User 11: ceDataInode=473434 installed=true hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=4
      firstInstallTime=2022-05-29 00:20:26
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
    User 13: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2022-05-29 00:20:26
      uninstallReason=0
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.OTHER_SENSORS: granted=false
    User 17: ceDataInode=0 installed=false hidden=false suspended=false distractionFlags=0 stopped=true notLaunched=true enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2022-05-29 00:20:26
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=false
        android.permission.OTHER_SENSORS: granted=false
  Package [com.android.health.connect.backuprestore] (641c342):
    appId=10180
    pkg=Package{c1209c3 com.android.health.connect.backuprestore}
    codePath=/apex/com.android.healthfitness/app/HealthConnectBackupRestore@UP1A.231105.001
    resourcePath=/apex/com.android.healthfitness/app/HealthConnectBackupRestore@UP1A.231105.001
    legacyNativeLibraryDir=/apex/com.android.healthfitness/app/HealthConnectBackupRestore@UP1A.231105.001/lib
    extractNativeLibs=false
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=34 minSdk=34 targetSdk=34
    minExtensionVersions=[]
    versionName=14
    usesNonSdkApi=true
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    dataDir=/data/user/0/com.android.health.connect.backuprestore
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=1970-01-01 01:00:00
    lastUpdateTime=1970-01-01 01:00:00
    installerPackageName=null
    installerPackageUid=-1
    initiatingPackageName=null
    originatingPackageName=null
    packageSource=0
    appMetadataFilePath=null
    signatures=PackageSignatures{279c240 version:3, signatures:[e1bc9c21], past signatures:[]}
    installPermissionsFixed=false
    pkgFlags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP ]
    privatePkgFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    apexModuleName=com.android.healthfitness
    declared permissions:
      android.permission.HEALTH_CONNECT_BACKUP_INTER_AGENT: prot=signature|privileged
    install permissions:
      android.permission.HEALTH_CONNECT_BACKUP_INTER_AGENT: granted=true
    User 0: ceDataInode=1222730 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-m7C5.frro
        /data/resource-cache/com.android.systemui-accent-rxem.frro
        /data/resource-cache/com.android.systemui-dynamic-DiUC.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.READ_PHONE_STATE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|RESTRICTION_UPGRADE_EXEMPT]
    User 10: ceDataInode=1389570 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-08ws.frro
        /data/resource-cache/com.android.systemui-accent-fhcL.frro
        /data/resource-cache/com.android.systemui-dynamic-kZ92.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.READ_PHONE_STATE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|RESTRICTION_UPGRADE_EXEMPT]
    User 11: ceDataInode=1194229 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-E1GA.frro
        /data/resource-cache/com.android.systemui-accent-QRHM.frro
        /data/resource-cache/com.android.systemui-dynamic-arH4.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.READ_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|RESTRICTION_UPGRADE_EXEMPT]
        android.permission.READ_PHONE_STATE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED]
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false, flags=[ USER_SENSITIVE_WHEN_GRANTED|RESTRICTION_UPGRADE_EXEMPT]
    User 13: ceDataInode=0 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true
        android.permission.READ_EXTERNAL_STORAGE: granted=false
        android.permission.READ_PHONE_STATE: granted=false
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false
    User 17: ceDataInode=0 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      legacy overlay paths:
        /product/overlay/NavigationBarModeGestural/NavigationBarModeGesturalOverlay.apk
      runtime permissions:
        android.permission.OTHER_SENSORS: granted=true
        android.permission.READ_EXTERNAL_STORAGE: granted=false
        android.permission.READ_PHONE_STATE: granted=false
        android.permission.WRITE_EXTERNAL_STORAGE: granted=false
  
"""
# }}}

twitterNamePattern = r'\s*AppSettings:\s'

regexes = {
    'twitterID': r"\s*mId='(\d{3,24})'",
    # Usernames are 4-15 characters.
    # https://help.x.com/en/managing-your-account/x-username-rules
    'twitterHandle': r'mName=@\S{4,15}',
}
names = {
    'twitterID': 'Install time',
    'twitterHandle': 'Last updated',
}

packageList = []

with open('package.txt.priv', 'r') as file:
    fileContent = file.readlines()
    packageDict = {}
    for line in fileContent:
        match = re.match(twitterNamePattern, line)
        if not match == None:
            if len(packageDict) > 0: # current package has data, but we've ran into a new Package [...] line
                packageList.append(packageDict) # so add it to the list of packages
                packageDict = {} # and clear the package, ready for next round

            packageDict['packageName'] = match[1]
            continue

        if len(packageDict) > 0: # are we filling in a package? (it's > 0 if packageName is set)
            for k, v in regexes.items(): # keys and values from dict
                match = re.match(v, line)
                if match:
                    packageDict[k] = match[1] # key has the same name as in package dictionary
                    break

    # after the last iteration, include the resulting package if it has data
    if len(packageDict) > 0:
        packageList.append(packageDict)


for packageDict in packageList:
    print(f"Package: {packageDict['packageName']}")
    for k, v in names.items():
       if k in packageDict:
          print(f'{v}: {packageDict[k]}')
    print()
