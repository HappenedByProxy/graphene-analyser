We collect data from ADB.
This data is stored in a zip. The only thing we need is the log that'll be like 60MB.
But there's a way to split this data into individual files, possibly? Not sure how to do that, if I gotta do it myself or maybe adb can do it...

SPLIT IT
https://developer.android.com/tools/dumpsys

"adb shell dumpsys -l" shows all the possible services we can dump. connecting my own phone gives:
  DockObserver
  SurfaceFlinger
  SurfaceFlingerAIDL
  accessibility
  account
  activity
  activity_task
  adb
  adservices_manager
  alarm
  android.frameworks.cameraservice.service.ICameraService/default
  android.frameworks.location.altitude.IAltitudeService/default
  android.frameworks.sensorservice.ISensorManager/default
  android.frameworks.stats.IStats/default
  android.hardware.authsecret.IAuthSecret/default
  android.hardware.camera.provider.ICameraProvider/internal/0
  android.hardware.cas.IMediaCasService/default
  android.hardware.contexthub.IContextHub/default
  android.hardware.drm.IDrmFactory/clearkey
  android.hardware.drm.IDrmFactory/widevine
  android.hardware.identity.IIdentityCredentialStore/default
  android.hardware.input.processor.IInputProcessor/default
  android.hardware.nfc.INfc/default
  android.hardware.oemlock.IOemLock/default
  android.hardware.power.IPower/default
  android.hardware.rebootescrow.IRebootEscrow/default
  android.hardware.thermal.IThermal/default
  android.hardware.usb.IUsb/default
  android.hardware.vibrator.IVibrator/default
  android.hardware.weaver.IWeaver/default
  android.hardware.wifi.IWifi/default
  android.hardware.wifi.supplicant.ISupplicant/default
  android.os.UpdateEngineService
  android.os.UpdateEngineStableService
  android.security.apc
  android.security.authorization
  android.security.compat
  android.security.identity
  android.security.legacykeystore
  android.security.maintenance
  android.security.metrics
  android.system.keystore2.IKeystoreService/default
  android.system.net.netd.INetd/default
  android.system.suspend.ISystemSuspend/default
  app_binding
  app_hibernation
  app_integrity
  app_search
  appops
  appwidget
  attestation_verification
  audio
  auth
  autofill
  background_install_control
  backup
  battery
  batteryproperties
  batterystats
  binder_calls_stats
  biometric
  blob_store
  bluetooth_manager
  bugreport
  cacheinfo
  carrier_config
  clipboard
  color_display
  com.google.hardware.pixel.display.IDisplay/default
  companiondevice
  connectivity
  connectivity_native
  connmetrics
  content
  contexthub
  country_detector
  cpuinfo
  credential
  crossprofileapps
  dataloader_manager
  dbinfo
  device_config
  device_identifiers
  device_lock
  device_policy
  device_state
  deviceidle
  devicestoragemonitor
  diskstats
  display
  domain_verification
  dreams
  drm.drmManager
  dropbox
  dynamic_system
  econtroller
  emergency_affordance
  ethernet
  euicc_card_controller
  external_vibrator_service
  feature_flags
  file_integrity
  fingerprint
  font
  game
  gfxinfo
  gpu
  grammatical_inflection
  graphicsstats
  gsiservice
  hardware_properties
  healthconnect
  imms
  incidentcompanion
  incremental
  input
  input_method
  inputflinger
  ions
  iphonesubinfo
  ipsec
  isms
  isub
  jobscheduler
  launcherapps
  legacy_permission
  lights
  locale
  location
  location_time_zone_manager
  lock_settings
  logcat
  logd
  looper_stats
  manager
  media.aaudio
  media.audio_flinger
  media.audio_policy
  media.camera
  media.camera.proxy
  media.extractor
  media.metrics
  media.player
  media.resource_manager
  media.resource_observer
  media_communication
  media_metrics
  media_projection
  media_resource_monitor
  media_router
  media_session
  meminfo
  memtrack.proxy
  midi
  mount
  nearby
  netd_listener
  netpolicy
  netstats
  network_management
  network_score
  network_stack
  network_time_update_service
  network_watchlist
  nfc
  notification
  oem_lock
  ondevicepersonalization_system_service
  overlay
  pac_proxy
  package
  package_native
  people
  performance_hint
  permission
  permission_checker
  permissionmgr
  persistent_data_block
  phone
  pinner
  platform_compat
  platform_compat_native
  power
  powerstats
  print
  processinfo
  procstats
  qchook
  rcs
  reboot_readiness
  recovery
  remote_provisioning
  resources
  restrictions
  role
  rollback
  runtime
  safety_center
  scheduling_policy
  sdk_sandbox
  search
  sec_key_att_app_id_provider
  secure_element
  security_state
  sensor_privacy
  sensorservice
  serial
  servicediscovery
  settings
  shortcut
  simphonebook
  slice
  soundtrigger
  soundtrigger_middleware
  speech_recognition
  stats
  statsbootstrap
  statscompanion
  statsmanager
  statusbar
  storaged
  storaged_pri
  storagestats
  system_config
  system_server_dumper
  system_update
  tare
  telecom
  telephony.registry
  telephony_ims
  testharness
  tethering
  textclassification
  textservices
  texttospeech
  thermalservice
  time_detector
  time_zone_detector
  tracing.proxy
  transparency
  trust
  uce
  uimode
  updatelock
  uri_grants
  usagestats
  usb
  user
  vcn_management
  vendor.google.google_battery.IGoogleBattery/default
  vibrator_manager
  virtualdevice
  voiceinteraction
  vpn_management
  wallpaper
  wearable_sensing
  webviewupdate
  wifi
  wifiaware
  wifinl80211
  wifip2p
  wifirtt
  wifiscanner
  window

FINALLY DOCUMENTATION:
https://developer.android.com/reference/android/app/Service

Generally, we have found the following to be the most valuable:
account = Detailed info about almost all accounts logged into on the profile.
settings = Info about all settings on the device.
wifi = Wifi network history.
  WifiConfigManager - Configured networks Begin
wifiscanner = Outputs the current nearby networks, but also stores a history.
vpn_management = VPNs that have been used. Example, net.mullvad.mullvadvpn.
storaged = List of installed applications? Might shown per-profile too?
power = Whats waking up the phone?
package = Every single package installed.
usagestats = Every single app you've ever installed, and app usage stats! GREAT!!
  Token 85: [com.android.permissioncontroller
  
content = Shows accounts in a weird way.
notification = Notifications, for some reason also shows all added Twitter accounts...
  AppSettings: com.twitter.android
user = Like account, but shows more data about the profile, including last logged in, flags, the FINGERPRINT ID??




Possibly valuable:
biometric
window
vibrator_manager = History of all vibration events and what caused them. Example, NOTIFICATION, HARDWARE_FEEDBACK
tethering = Everytime it was connected to a computer?
telecom = Recent calls?
search = Searchable authorities
meminfo = Does a memory dump.
meminfo <package> = Specifically shows mmemory info about that package.
cpuinfo = CPU utilization.
platform_compat = i dont even know
phone = Roaming operating number?
shortcut = Shows some SMS contacts but only for QKSMS?
  Package: com.moez.QKSMS
.





Not working services:
reboot_readiness
recovery
restrictions
qchook
people
permission
oem_lock

Not useful, I think:
runtime
print
resources
pinner
persistent_data_block
nfc = Does a "NFCSnoop" dump.
>Turns out, Android saves a ring buffer full of all NFC interactions in NCI (so between the phone and the actual NFC chip in the phone). You can extract them with the command above.
https://forum.dangerousthings.com/t/nfcsnoop-decoder-android-nfc-snooping/9962
https://github.com/vivokey/NFCSnoopDecoder

I decoded a snippet, it spits out an even longer output. This is raw nfc data. I dont' know what I can use this for. This isn't worth it

CLI? GUI? Both?

For example;

DUMPSYS settings:
GLOBAL SETTINGS (user 0)
version: 212
_id:402 name:adb_wifi_enabled pkg:android value:0 default:0 defaultSystemSet:true
_id:42 name:low_battery_sound_timeout pkg:android value:0 default:0 defaultSystemSet:true
_id:78 name:wear_os_version_string pkg:android value: default: defaultSystemSet:true
_id:34 name:car_undock_sound pkg:android value:/product/media/audio/ui/Undock.ogg default:/product/media/audio/ui/Undock.ogg defaultSystemSet:true
_id:64 name:obtain_paired_device_location pkg:android value:1 default:1 defaultSystemSet:true
_id:340 name:enable_freeform_support pkg:com.android.settings value:0 default:0 defaultSystemSet:true
_id:337 name:show_notification_channel_warnings pkg:com.android.settings value:0 default:0 defaultSystemSet:true
_id:84 name:system_capabilities pkg:android value:99 default:99 defaultSystemSet:true
_id:113 name:apm_enhancement_enabled pkg:android value:0 default:0 defaultSystemSet:true
_id:95 name:ambient_plugged_timeout_min pkg:android value:-1 default:-1 defaultSystemSet:true
_id:404 name:development_settings_enabled pkg:com.android.settings value:1 default:1 defaultSystemSet:true
_id:10 name:window_animation_scale pkg:android value:1.0 default:1.0 defaultSystemSet:true
_id:344 name:stylus_handwriting_enabled pkg:com.android.settings value:0 default:0 defaultSystemSet:true

(snippet)

_id:402 name:adb_wifi_enabled pkg:android value:0 default:0 defaultSystemSet:true

id: unique identifier within system db
name: name of the setting
pkg: the package that owns/controls the setting
value: what its set to, 0 = false, 1 = true
defaultSystemSet: default system value

POSSIBLE VIEW:
--------------------------------------------------------------------------
| id | name | pkg | value | default | defaultSystemSet | description     |
| 402| adb_wifi_enabled | android | 0 | 0 | If ADB over Wi-Fi is enabled |
--------------------------------------------------------------------------

ALT:
--------------------------------------------------------------------------
| id | name | pkg | value | default | defaultSystemSet | description     |
| 402| ADB over WiFi | android | 0 | 0 | If ADB over Wi-Fi is enabled    |
--------------------------------------------------------------------------

CODE???:
Use some code to seperate this string into different parts and save as a struct
_id:402 
name:adb_wifi_enabled 
pkg:android 
value:0 
default:0 
defaultSystemSet:true

WHAT IS STRUCT?:
a struct is a collection of variables

DESCRIPTIONS:
eventually our DB of setting descriptions and clean names will be quite big, so putting it into the same .go file isn't very pretty... instead, lets put it into a JSON which is just as ugly. least then it looks cooler in a repo.

NAMES:
{
  "adb_wifi_enabled": "ADB over Wi-Fi."
}

DESC:
{
  "adb_wifi_enabled": "Enable/disable ADB over Wi-Fi."
}

OUTPUT:
--------------------------------------------------------------------------
| id | name | pkg | value | default | defaultSystemSet | description     |
| 402| <NAMES.JSON> | android | 0 | 0 | <DESC.JSON>                      |
--------------------------------------------------------------------------

MODULES:
https://github.com/pterm/pterm/


### Usagestats
Some services need to be understood before others can.
"usagestats" need knowledge from "account".
"usagestats" will output a history of all installed APKs under a token that seems to change, but so far starts with ": [com.android.permissioncontroller".
These all come under indents that belong to different users, to show that these apps were installed in a certain profile. For example, user=11 may have "com.badapp.1" listed in "usagestats". But, in "package" it's absent. Additionally, "com.badapp.1" only shows under user 11, and not user 0.

What happens if an entire profile is removed? What if we install stuff on the guest profile then wipe it?

I added a new user on my personal phone, "FLASHYNAME". I set it up.
Installed apps:
- Info : From "Apps"
- KurobaEx : From github

I opened KurobaEx, enabled notifs, added 4chan as a site, then added the /wsg/ board.
I opened a thread, "Ed Edd n Eddy", downloaded the first webm, saved it to Downloads/Ddd.

I made a bugreport with the profile open. Then I switched to the Owner profile, and deleted FLASHYNAME. Then I did another bugreport.

Before: FLASHYNAME appears 7 times.
After: FLASHYNAME never appears.
After reboot: FLASHYNAME never appears.

FLASHYNAME's ID is 14.
Before: 358 results for "userid=14", 378 results for "user=14", 768 results for "user 14"
After: 226 results for "userid=14", 60 results for "user=14", 577 results for "user 14".
After reboot: 0 results for "userid=14", 15 results for "user=14", 1 results for "user 14".

We know KurobaEx was installed on user 14, but this may have been just the latest installed application?
  Session 1587917642:
    userId=14 mOriginalInstallerUid=1410028 mOriginalInstallerPackageName=com.android.packageinstaller 
    installerPackageName=com.android.packageinstaller installInitiatingPackageName=com.android.packageinstaller 
    installOriginatingPackageName=org.chromium.chrome mInstallerUid=1410028 createdMillis=1719595345907 
    updatedMillis=1719595364364 committedMillis=1719595350972 stageDir=/data/app/vmdl1587917642.tmp stageCid=null 
    mode=1 installFlags=0x404012 installLocation=1 installReason=4 installScenario=0 sizeBytes=42928 appPackageName=com.
    github.k1rakishou.chan appIcon=false appLabel=null originatingUri=https://github.com/K1rakishou/Kuroba-Experimental/
    releases/download/v1.3.33-release/KurobaEx.apk originatingUid=1410085 referrerUri=https://github.com/K1rakishou/Kuro
    ba-Experimental/releases/tag/v1.3.33-release abiOverride=null volumeUuid=null mPermissionStates={android.permission.
    USE_FULL_SCREEN_INTENT=2} packageSource=4 whitelistedRestrictedPermissions=null autoRevokePermissions=3 installerPac
    kageName=null isMultiPackage=false isStaged=false forceQueryable=false requireUserAction=UNSPECIFIED requiredInstall
    edVersionCode=-1 dataLoaderParams=null rollbackDataPolicy=0 rollbackLifetimeMillis=0 applicationEnabledSettingPersis
    tent=false developmentInstallFlags=0x0 unarchiveId=-1 unarchiveIntentSender=null 
    mClientProgress=1.0 mProgress=0.90000004 mCommitted=true mPreapprovalRequested=false mSealed=true 
    mPermissionsManuallyAccepted=false mStageDirInUse=true mDestroyed=true mFds=0 mBridges=1 mFinalStatus=1 
    mFinalMessage=Session installed mParentSessionId=-1 mChildSessionIds=[] mSessionApplied=true mSessionFailed=false 
    mSessionReady=false mSessionErrorCode=1 mSessionErrorMessage= mPreapprovalDetails=null 



"textclassification" = Number user states:
User=14 
    Default: context=android.app.ContextImpl@e6556c1 userId=14 packageName=android.ext.services **installed=false enabled=false** boundComponentName=null isTrusted=true bindServiceFlags=67108865 boundServiceUid=-1 binding=false numOfPendingRequests=0 

user=14
userid=14