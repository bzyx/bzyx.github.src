Building and booting Nexus 5 kernel
###############################################
:date: 2014-05-06 15:30
:tags: english, master's thesis, linux
:lang: en
:author: Marcin Jabrzyk
:summary: I've read a lot of tutorials, articles, descriptions about build Android and non-Android Linux kernels. Many of them didn't work at all, some of them partly, and I will try to write one from the bottom up which will work for at least one device - Nexus 5.

My description of building process will strongly base on this article which was a great help in whole process: http://pete.akeo.ie/2013/10/compiling-and-running-your-own-android.html


Prerequisites:

- You should own a Nexus 5 device, with unlocked bootloader (and for best experience rooted)
- Android SDK tools in your PATH (adb and fastboot needed)
- Decent internet connection
- git installed, with other classical tools needed for kernel building

These are the thing I'll not cover in the article, as they are basics and not most important in whole process.

You should really start with official Google guide here_ . I'll describe the process from my own perspective i.e. Ubuntu 14.04 x64 machine.
So let's start with our tools. I assume you are working in some new empty folder. First is toolchain:

.. code-block:: bash
    :anchorlinenos:

    $ git clone https://android.googlesource.com/platform/prebuilts/gcc/linux-x86/arm/arm-eabi-4.7/

        Cloning into 'arm-eabi-4.7'...
        remote: Sending approximately 23.63 MiB ...
        remote: Counting objects: 22, done
        remote: Finding sources: 100% (22/22)
        remote: Total 201 (delta 89), reused 201 (delta 89)
        Receiving objects: 100% (201/201), 23.63 MiB | 585.00 KiB/s, done.
        Resolving deltas: 100% (89/89), done.
        Checking connectivity... done.

The never 4.8 compilers suite seems to not working with Nexus 5 kernel sources at this moment. The same applies to androideabi version.
Now we'll create a file with environment variables which are going to help us in simpling the process.

.. code-block:: bash

    $ vim run_this_android.sh

Fill it with:

.. code-block:: bash

    export CC=$(pwd)/arm-eabi-4.7/bin/arm-eabi-
    export CROSS_COMPILE=$(pwd)/arm-eabi-4.7/bin/arm-eabi-

    export ARCH=arm
    export SUBARCH=arm

    export PATH=$PATH:$(pwd)/andorid_boot_tools_bin

Make it runnable and source to current terminal window.

.. code-block:: bash

     $ chmod +x run_this_android.sh
     $ source run_this_android.sh

Now it's time to clone the actual kernel sources (it will take some time).

.. code-block:: bash

     $ git clone https://android.googlesource.com/kernel/msm.git

        Cloning into 'msm'...
        remote: Sending approximately 753.86 MiB ...
        remote: Counting objects: 52377, done
        remote: Finding sources: 100% (4982/4982)
        remote: Total 3288741 (delta 2746117), reused 3287961 (delta 2746117)
        Receiving objects: 100% (3288741/3288741), 754.56 MiB | 601.00 KiB/s, done.
        Resolving deltas: 100% (2753582/2753582), done.
        Checking connectivity... done.

Next thing we do is change branch to the proper one (to get best result you shout checkout to a commit in your current kernel version 3.4.0-gXXXXXXX, where XXXXXXX is short of commit SHA-1).

.. code-block:: bash

    $ cd msm/
    $ git branch -a

      * master
        remotes/origin/HEAD -> origin/master
        remotes/origin/android-msm-2.6.35
        remotes/origin/android-msm-3.9-usb-and-mmc-hacks
        remotes/origin/android-msm-flo-3.4-jb-mr2
        remotes/origin/android-msm-flo-3.4-kitkat-mr0
        remotes/origin/android-msm-flo-3.4-kitkat-mr1
        remotes/origin/android-msm-hammerhead-3.4-kitkat-mr1
        remotes/origin/android-msm-hammerhead-3.4-kk-fr1
        remotes/origin/android-msm-hammerhead-3.4-kk-fr2
        remotes/origin/android-msm-hammerhead-3.4-kk-r1
        remotes/origin/android-msm-mako-3.4-jb-mr1
        remotes/origin/android-msm-mako-3.4-jb-mr1-fr
        remotes/origin/android-msm-mako-3.4-jb-mr1-kgsl
        remotes/origin/android-msm-mako-3.4-jb-mr1.1
        remotes/origin/android-msm-mako-3.4-jb-mr2
        remotes/origin/android-msm-mako-3.4-kitkat-mr0
        remotes/origin/android-msm-mako-3.4-kitkat-mr1
        remotes/origin/android-msm-sony-cm-jb-3.0
        remotes/origin/master


   $ git checkout origin/android-msm-hammerhead-3.4-kitkat-mr1

Now we should have the code on which we can work :) So lets compile it, and check if it works for us.
In menuconfig *General setup ---> Local version - append to kernel release* you can append some string that you'll know that it's your kernel.

.. code-block:: bash

    $ make hammerhead_defconfig
    $ make menuconfig
    $ make -j4

Make some break while it's compiling. You should adjust the number -jX to the number of cores in your CPU.
If all went fine, at the end of output you'll find something like this:

.. code-block:: none

    OBJCOPY arch/arm/boot/zImage
    Kernel: arch/arm/boot/zImage is ready
    CAT     arch/arm/boot/zImage-dtb
    Kernel: arch/arm/boot/zImage-dtb is ready

You have your kernel ready. On most embedded systems that will be the end of our work. Usually you'll copy the kernel to SD card or NFS location, and the board will boot. But on Android it's different. We need to prepare special boot partition which then we can boot using fastboot.

So we need to start by downloading the image of Android for our phone from Google sites.
Go to Factory Images Nexus images_ site and download the image that corresponds to Android version that's on your phone. In my case it's 4.4.2_. Unpack it, then go inside and unpack the .zip archive. You need the boot.img file. Copy it to new folder inside directory where you downloaded the toolchain and kernel eg. *boot_img directory*.

Next thing we'll do is to prepare some special image crafting tools that Pete_ Batard prepared for us and put on his github_. I've made a copy of them on mine_ too.

Build this on different terminal window, if you've before sourced run_this_android.sh. On other way gcc will try to cross compile it for ARM architecture...

.. code-block:: bash

    $ cd .. # if you was in msm directory
    $ git clone https://github.com/pbatard/bootimg-tools.git

        Cloning into 'bootimg-tools'...
        remote: Reusing existing pack: 49, done.
        remote: Total 49 (delta 0), reused 0 (delta 0)
        Unpacking objects: 100% (49/49), done.
        Checking connectivity... done.

    $ cd bootimg-tools/
    $ make

        cc -Wall -Wextra -Wno-unused-parameter -pedantic -pipe -std=c99 -D_GNU_SOURCE -Iinclude   -c -o libmincrypt/sha.o libmincrypt/sha.c
        cc -Wall -Wextra -Wno-unused-parameter -pedantic -pipe -std=c99 -D_GNU_SOURCE -Iinclude   -c -o libmincrypt/rsa.o libmincrypt/rsa.c
        cc -Wall -Wextra -Wno-unused-parameter -pedantic -pipe -std=c99 -D_GNU_SOURCE -Iinclude   -c -o libmincrypt/sha256.o libmincrypt/sha256.c
        cc -Wall -Wextra -Wno-unused-parameter -pedantic -pipe -std=c99 -D_GNU_SOURCE -Iinclude   -c -o mkbootimg/mkbootimg.o mkbootimg/mkbootimg.c
        cc -o mkbootimg/unmkbootimg mkbootimg/unmkbootimg.o

    $ cd cpio/
    $ gcc mkbootfs.c  -o mkbootfs -I../include

    $ cd ../..
    $ mkdir andorid_boot_tools_bin
    $ cd andorid_boot_tools_bin/
    $ cp ../bootimg-tools/mkbootimg/mkbootimg .
    $ cp ../bootimg-tools/mkbootimg/unmkbootimg .
    $ cp ../bootimg-tools/cpio/mkbootfs .
    $ cd ..

It’s high time to unpack our boot partition from original image and prepare our own. So let's start.

.. code-block:: bash

    $ unmkbootimg -i boot_img/boot.img

        kernel written to 'kernel' (8331496 bytes)
        ramdisk written to 'ramdisk.cpio.gz' (498796 bytes)

        To rebuild this boot image, you can use the command:
        mkbootimg --base 0 --pagesize 2048 --kernel_offset 0x00008000 --ramdisk_offset 0x02900000 --second_offset 0x00f00000 --tags_offset 0x02700000 --cmdline 'console=ttyHSL0,115200,n8 androidboot.hardware=hammerhead  user_debug=31 maxcpus=2 msm_watchdog_v2.enable=1' --kernel kernel --ramdisk ramdisk.cpio.gz -o boot_img/boot.img


Change the kernel to the one that we've compiled.

.. code-block:: bash

    $ cp msm/arch/arm/boot/zImage-dtb kernel
    $ mkbootimg --base 0 --pagesize 2048 --kernel_offset 0x00008000 --ramdisk_offset 0x02900000 --second_offset 0x00f00000 --tags_offset 0x02700000 --cmdline 'console=ttyHSL0,115200,n8 androidboot.hardware=hammerhead  user_debug=31 maxcpus=2 msm_watchdog_v2.enable=1' --kernel kernel --ramdisk ramdisk.cpio.gz -o boot.img
    $ ls
        andorid_boot_tools_bin  arm-eabi-4.7  boot_img  boot.img  bootimg-tools  kernel  msm  ramdisk.cpio.gz  run_this_android.sh

In output of ls command we should see the boot.img file. If we have it, we've done :)
So let's try our work if it works or not. Connect your phone using USB cable to your PC, be sure that you have USB debugging enabled.

.. code-block:: bash

    $ adb start-server
        * daemon not running. starting it now on port 5037 *
        * daemon started successfully *
    $ adb reboot bootloader
    $ sudo fastboot boot boot.img

During this commands your phone will reboot to bootloader mode, next using fastboot command we'll copy the new boot image to RAM of the phone and boot it. **YOUR FLASH IS NOT TOUCHED IT'S 100% SAFE!**
Now just check in settings what is version of your kernel. When you've done with hacking, and want to have the original just reboot your phone. Happy hacking!

.. image:: |filename| /images/2014/Screenshot_2014-05-06-12-35-02.png
    :alt: "My settings in Android"

.. raw:: html

    <br/>
    <br/>

Im really thankful to Pete Batard for his original article and the tools he prepared. It save me ~20 GB of download the AOSP and much of frustration. Thank you! (:



.. _here: http://source.android.com/source/building-kernels.html
.. _images: https://developers.google.com/android/nexus/images#hammerhead
.. _4.4.2: https://dl.google.com/dl/android/aosp/hammerhead-kot49h-factory-02006b99.tgz
.. _Pete: https://github.com/pbatard
.. _github: https://github.com/pbatard/bootimg-tools
.. _mine: https://github.com/bzyx/bootimg-tools