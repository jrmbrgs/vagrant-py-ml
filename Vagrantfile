# -*- mode: ruby -*-

Vagrant.configure("2") do |config|
  config.vm.box = "debian/jessie64"


  # config.vm.network "forwarded_port", guest: 80, host: 8080
  # config.vm.network "private_network", ip: "192.168.33.10"
  # config.vm.network "public_network"

  config.vm.synced_folder "./ml", "/ml"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = true
    vb.memory = "1024"
    config.vm.provision "shell", path: "provision.sh"
  end
end
