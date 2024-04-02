---
title: Encrypting a partition and exporting it as rootfs
```

### Step 1: Creating a Virtual Disk
To begin, we'll create a virtual disk image that will act as our encrypted partition. We can use the `dd` command to create a file of a specified size filled with zeros:

```bash
dd if=/dev/zero of=virtual_disk.img bs=1M count=1024
```

This command creates a file named "virtual_disk.img" with a size of 1024 megabytes (1 GB).

### Step 2: Associating the Virtual Disk with a Loop Device
Next, we need to make the virtual disk image accessible as a block device. We can achieve this by associating it with a loop device using the `losetup` command:

```bash
sudo losetup -fP virtual_disk.img
```

You can now check what loop devices are available for you.

```bash
losetup -a
```

Replace `loopX` in the following commands with the correct loop device (will have the `virtual_disk.img` attached to the text).

### Step 3: Encrypting the Virtual Disk

Now that we have a virtual disk set up, let's encrypt it using `cryptsetup` and LUKS. In this example, we'll use a passphrase "cafebabe" for encryption. It's important to choose a strong passphrase in real-world scenarios.

```bash
echo -n cafebabe | sudo cryptsetup luksFormat /dev/loopX -
```

Replace "/dev/loopX" with the actual loop device assigned to your virtual disk (e.g., /dev/loop2).

### Step 4: Opening the Encrypted Disk
To access the encrypted disk, we need to open (decrypt) it using the same passphrase:

```bash
echo -n cafebabe | sudo cryptsetup open /dev/loopX my_encrypted_vp -
```

This command decrypts the virtual disk and maps it to a new device at "/dev/mapper/my_encrypted_vp".

### Step 5: Creating a Filesystem
After decrypting the virtual disk, we need to create a filesystem on it to store our files:

```bash
sudo mkfs.ext4 /dev/mapper/my_encrypted_vp
```

### Step 6: Mounting the Encrypted Volume
Finally, we can mount the decrypted volume to a mount point to access and modify its contents:

```bash
sudo mount /dev/mapper/my_encrypted_vp /mnt/encrypted_vp
```

### Step 7: Accessing the Encrypted Contents
With the encrypted volume mounted, we can now peek inside and browse its contents using standard Linux commands like `ls`:

```bash
ls -l /mnt/encrypted_vp
```

This command will display the files and directories stored within the encrypted virtual disk.

### Step 8: Locking the partition again

To unlock and access the contents of an encrypted volume using LUKS, first, ensure the encrypted device is associated with a loop device. Use `echo -n [passphrase] | sudo cryptsetup open /dev/loopX my_encrypted_vp -` to unlock, replacing `[passphrase]` with your actual passphrase and `/dev/loopX` with your loop device. After unlocking, mount it using `sudo mount /dev/mapper/my_encrypted_vp /mnt/encrypted_vp` to access its contents. To relock, start by unmounting with `sudo umount /mnt/encrypted_vp`. Finally, close the encrypted device using `sudo cryptsetup close my_encrypted_vp`, securing its contents until the next unlock. This process ensures data security, allowing access only to those with the passphrase.

> passphrase for us is cafebabe

```bash
sudo umount /mnt/encrypted_vp
sudo cryptsetup close my_encrypted_vp
```

## Performing an update via a `rootfs`

You might decide you need to do OTAs or some other form of updates, the easiest way to go about this on another's system with an encrypted disk is to create a `rootfs.tar`.

`rootfs.tar` typically refers to a compressed archive file containing the root filesystem of a Linux-based operating system. The "root filesystem" (rootfs) is the top-level directory hierarchy in a Linux system, containing essential directories like `/bin`, `/etc`, `/lib`, `/sbin`, `/usr`, and `/var`.

This archive often contains all the files and directories necessary for the operating system to function properly. It includes system binaries, libraries, configuration files, device files, and other essential components.

Archiving the root filesystem into a `rootfs.tar` file is a common practice for system backups, cloning, or distribution. It allows for easy transfer, duplication, and restoration of the entire operating system environment.

#### How to export a `rootfs.tar`

`sudo tar -czpvf rootfs.tar -C /mnt/encrypted_vp .`

[under construction]
