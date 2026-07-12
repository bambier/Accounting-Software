[app]
; pysidedeploy.spec — ganzabara
;
; consumed by `pyside6-deploy` (nuitka backend). run from the project root = 
;   pyside6-deploy -c pysidedeploy.spec --dry-run   # verify config first
;   pyside6-deploy -c pysidedeploy.spec             # produce the binary
; ---------------------------------------------------------------------------
; license / supported platforms notice
; ganzabara is distributed under the proprietary nchl-1.1 license (vahrka).
; section 3.e of that license prohibits compiling or building this software
; for macos or ios without a signed commercial agreement. `src/main.py`
; enforces this at runtime with a hard guard; this spec enforces it at build
; time by only targeting windows and linux. do not add a `macos` section or
; run this spec on a darwin host. contact vahrka (licensing) for commercial
; macos/ios builds.

# title of your application
title = Ganzabara

# project root directory. default = The parent directory of input_file
project_dir = ./src/

# source file entry point path. default = main.py
input_file = src/main.py

# directory where the executable output is generated
exec_directory = ./deployment

# path to the project file relative to project_dir
project_file = pyproject.toml

# application icon
icon = src/resources/images/icon.ico

[python]

# python path
python_path = /home/nima/Desktop/python-projects/Accounting-Software/venv/bin/python

# python packages to install
# extra packages that are not auto-detected by nuitka's import scanner because
# they are imported dynamically (plugin loader) or via pyside6 resource system
packages = PySide6==6.11.1,shiboken6==6.11.1,peewee==4.1.2,jdatetime==5.3.0,jalali_core==1.0.0,PyYAML==6.0.3,fpdf==1.7.2,numpy==2.5.1,pandas==3.0.3,python-dateutil==2.9.0.post0,six==1.17.0,httpx==0.28.1,httpcore==1.0.9,anyio==4.14.1,h11==0.16.0,certifi==2026.6.17,idna==3.18,Nuitka==4.1.3

# buildozer = for deploying Android application
android_packages = buildozer==1.5.0,cython==0.29.33

[qt]

# paths to required qml files. comma separated
# normally all the qml files required by the project are added automatically
# design studio projects include the qml files using qt resources
qml_files = 

# excluded qml plugin binaries
excluded_qml_plugins = 

# qt modules used. comma separated
modules = Core,DBus,Gui,Widgets

# qt plugins used by the application. only relevant for desktop deployment
# for qt plugins used in android application see [android][plugins]
plugins = accessiblebridge,egldeviceintegrations,generic,iconengines,imageformats,platforminputcontexts,platforms,platforms/darwin,platformthemes,styles,wayland-decoration-client,wayland-graphics-integration-client,wayland-shell-integration,xcbglintegrations

[android]

# path to pyside wheel
wheel_pyside = 

# path to shiboken wheel
wheel_shiboken = 

# plugins to be copied to libs folder of the packaged application. comma separated
plugins = 

[nuitka]
; nuitka build mode = 
;   standalone -> directory with exe/binary + dependent .so/.dll/.dat files
;                 (recommended default = faster startup, no self-extraction
;                 step, plays well with av/smartscreen, works naturally with
;                 installers like msi/nsis/deb/rpm/appimage, and lets you
;                 patch individual libraries between releases)
;   onefile    -> single self-contained executable that self-extracts to a
;                 temp dir at every launch. convenient for "download one
;                 file and run" distribution, but adds startup latency and
;                 is more likely to trip av/smartscreen heuristics. use only
;                 if you have a specific single-file distribution requirement.
mode = standalone
; compiler / python flags forwarded to nuitka. --no-debug strips debug info
; from the shipped binary (do not ship debug symbols in commercial builds).
extra_args = --quiet --noinclude-pytest-mode=nofollow --python-flag=no_docstrings --python-flag=-O --lto=yes --assume-yes-for-downloads

# usage description for permissions requested by the app as found in the info.plist file
# of the app bundle. comma separated
# eg = extra_args = --show-modules --follow-stdlib
macos.permissions = 
; --------------------------------------------------------------------- ;
; windows-specific packaging

[nuitka.windows]
; show a console window = disabled for a production GUI app
windows_console_mode = disable
; version-info resource embedded into the .exe (explorer "details" tab)
windows_company_name = Vahrka
windows_product_name = Ganzabara
windows_product_version = 1.0.0.0
windows_file_version = 1.0.0.0
windows_file_description = Ganzabara Accounting, Invoicing & Payroll Suite
windows_icon_from_ico = src/resources/images/icon.ico
; ---------------------------------------------------------------------
; security = code signing (mandatory for commercial distribution)
; ganzabara is a financial application handling sensitive customer data
; (invoices, payroll, bank feeds). an unsigned executable will trigger
; smartscreen / defender warnings and is not acceptable for commercial
; release. provide a valid authenticode certificate below before shipping;
; leave blank only for local/dev builds.
;
; windows_uac_admin = do NOT request admin rights globally — the app
;                             does not need elevated privileges to run.
windows_uac_admin = false
windows_uac_uiaccess = false
; populate these two for release builds (values intentionally left blank —
; do not commit real certificate paths/passwords to source control; inject
; via ci secret store / environment variable at build time instead) = 
windows_signing_certificate = 
windows_signing_certificate_password_env = GANZABARA_CODESIGN_PASSWORD
; --------------------------------------------------------------------- ;
; linux-specific packaging

[nuitka.linux]
; embed .png icon and generate a .desktop entry for installers (appimage/deb/rpm)
linux_icon = src/resources/images/icon.png
linux_desktop_file_generate = true
linux_desktop_categories = Office;Finance;
; linux_onefile_appimage packages the app as an appimage, which requires
; mode = onefile above. Left false to match the standalone default; flip
; both mode = onefile and this to true if you specifically need an AppImage.
linux_onefile_appimage = false
; --------------------------------------------------------------------- ;
; macos — intentionally unsupported, see notice at top of file.
; a [nuitka.macos] section is deliberately omitted. do not add one without
; a commercial license amendment from vahrka;
; android packaging (buildozer, via pyside6-android-deploy)

[buildozer]
mode = true
title = Ganzabara
package.name = ganzabara
package.domain = vahrka.software
version = 1.0.0
; recipes for pure-python/native deps that need android cross-compilation.
; numpy/pandas require the python-for-android numpy recipe; fpdf2 and
; pyyaml/python-dateutil/peewee/jdatetime are pure python and ship as-is.
requirements = python3,PySide6==6.11.1,shiboken6==6.11.1,peewee==4.1.2,jdatetime==5.3.0,jalali_core==1.0.0,PyYAML==6.0.3,fpdf==1.7.2,numpy==2.5.1,pandas==3.0.3,python-dateutil==2.9.0.post0,six==1.17.0,httpx==0.28.1,httpcore==1.0.9,anyio==4.14.1,h11==0.16.0,certifi==2026.6.17,idna==3.18
; api levels — target current play store minimum, min covers most devices
android_minapi = 24
android_target_api = 34
android_ndk_api = 24
android.archs = arm64-v8a,armeabi-v7a
; app icon / presplash
icon.filename = src/resources/images/icon.png
presplash.filename = src/resources/images/icon.png
; permissions — keep minimal; only storage for local sqlite db + backups
; and network for the (stubbed) bank-feed service.
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
; ---------------------------------------------------------------------
; security = Android release signing (mandatory for commercial/Play Store)
; never commit a real keystore or password to source control — inject via
; ci secret store / environment variables at build time.
android.release_artifact = aab
android.keystore = 
android.keystore_password_env = GANZABARA_ANDROID_KEYSTORE_PASSWORD
android.keyalias_password_env = GANZABARA_ANDROID_KEYALIAS_PASSWORD


; --------------------------------------------------------------------- ;
; macos / ios — intentionally unsupported, see notice at top of file
; (license §3.e). no [nuitka.macos] section and no ios buildozer target
; are included. do not add either without a commercial license amendment.

