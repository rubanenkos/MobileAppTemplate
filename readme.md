# Mobile application template for running tests on mobile android emulator

For setting up the right infrastructure to run tests you need to do the following:
- Install Android Studio
- Start default application and run emulator (AVD manager button)
- Create virtual device and save settings
- Install and setup Appuim

Before run be sure that all env variables are set it
See the example below:
```
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-12.0.2.jdk/Contents/Home
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_202.jdk/Contents/Home
export ANDROID_HOME=/Users/user/Library/Android/sdk
export PATH=$ANDROID_HOME/platform-tools:$PATH
export PATH=$ANDROID_HOME/tools:$PATH
export PATH=$ANDROID_HOME/tools/bin:$PATH
```

For element inpection you can use app uiautomatorviewer (use console to run) or Appium default instrument
From Appuim app press "Start inspector session" to get an opportunity to find elements
Use the following for the device emulator:
```
{
  "deviceName": "Pixel 2 API 26",
  "platformName": "Android",
  "version": "8+"
}
```


**P/S Useful video and articles:**
- https://www.swtestacademy.com/how-to-install-appium-on-mac/
- Python, Behave & Appium | Svetlana Levinsohn
https://www.youtube.com/watch?v=jnKd6PRhmDY&ab_channel=JobEasy
- Appium Python Tutorial - Python and Pycharm Installation
https://www.youtube.com/watch?v=biqYLYJZgEM&list=PLWIBmxdTr81dDEZRiNxoy55dIDWtMyOoc&ab_channel=CopeAutomation

