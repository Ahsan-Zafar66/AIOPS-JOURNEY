Vagrant.configure("2") do |config|
 config.vm.define "web" do |web|
  web.vm.provider "virtualbox" do |vb_web|
    vb_web.memory = 1024
    vb_web.cpus = 2 
  end 

     web.vm.box = "ubuntu/trusty64"
     web.vm.network "private_network", ip: "192.168.33.20"
     web.vm.provision "shell",
      inline: "sudo touch /home/vagrant/web.txt"
 end

  config.vm.define "mysql" do |mysql|
    mysql.vm.box = "samdoran/rhel7"
    mysql.vm.network "private_network", ip: "192.168.33.21"
    mysql.vm.provision "shell",
      inline: "sudo touch /home/vagrant/mysql.txt"
  end
end
