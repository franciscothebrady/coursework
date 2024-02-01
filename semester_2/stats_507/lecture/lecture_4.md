## 2024-01-24
cloud computing 

### cloud 
- you used to need whole server setups to run a company
- now you can just rent resources from a cloud computing provider

### cloud computing
- on demand self-service: no human intervention needed
- broad network access: access from anywhere
- resource pooling: many users share the same physical hardware
- rapid elasticity: scale up and down as needed
- measured service: pay only for what you use

### terms
- cloud computing is delivery of computing services--servers, storage, security, software stack, analytics-- over the internet.
- companies offering these services are called cloud providers and typically charge for cloud computing services based on usage, similar to how you are billed for water or electricity at home.
- it can be accessed by anyone and from anywhere with a device or a computer from the internet.

### service models
- IAAS - infrastructure as a service -- compute engine, raw compute, storage, network. pay for what you allocate.
- PAAS - platform as a service -- app engine: your application code can use service libraries to use the infrastructure. pay for what you use.
- SAAS - software as a service -- gmail, google docs, etc. consumed directly by the user.

### advantages of cloud systems
- don't need to maintain
- can scale system vertically or horizontally
- flexibility: ideal for businesses with growing or fluctuating bandwidth demands
- disaster recovery: data is stored in the cloud, so it is easier to recover
- automatic software updates: no need to worry about updating software
- capital-expenditure free
- collaboration

### popular cloud providers
- amazon web services: ec2, s3
- google cloud platform: compute engine, cloud storage

### typical features to compare
- API
    - multiple api or open standard
- availability zones:
    - isolate parts of the cloud for specific purposes
- fault tolerance/failover
    - two instances of the same VM on two different physical machines. one physical machine goes down, will the other one take over?
- live migration
    - moving a virtual machine while it is running

### early container concepts
- level 1: computer hardware
- level 2: operating system
- level 3: JRE, JDK, JVM
    - JRE: java runtime environment
    - JDK: java development kit
    - JVM: java virtual machine
- level 4: java application

bottom line: this architecture allows you to run java applications on any operating system

### virtualization
- virtual machine: virtualization of a physical computer as a complete hardward platform with OS, CPU, memory, etc.
- container: is a virtualization runtime environment that runs on top of the OS jernal and emulates an operating system rather than the underlying hardware.
- hypervisor: a hypervisor is a process that separates a computers operating system and applications from the underlying physical hardware. the hypervisor allocates the CPU resources, memory, and other resources to each virtual machine as needed.

### how do virtual machines and containers differ?
- hypervisor: a virtual machine manager that allows multiple operating systems to share a single hardware host
- container runtime: a container runtime environment that runs on top of the OS kernel and emulates an operating system rather than the underlying hardware.

### why use containers?
- consistency: across development, testing, and production environments
- loose coupling: between application and operating system layers
- workload migration: simplified between on-premises and cloud environments
- agility: agile development and operations

### cloud platform architecture
1. need a specific OS?
2. handle the MAP and IP addresses of a VM
3. which hypervisor is supported?
4. repository of disk images
5. front-end for users
6. the cloud platform

### kubernetes
- container cluster orchestration system
- pod: a group of containers that are deplored together, with guaranteed network access
- help developers build modularly

