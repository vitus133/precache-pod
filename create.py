#!/usr/bin/python3
import yaml

with open("pod-default.yaml", "r") as p:
    pod = yaml.load(p)

with open("images", "r") as f:
    images = f.readlines()

containers = []
idx = 0
for image in images:
    container = {}
    container["name"] = f"test-{idx}"
    container["resources"] = {}
    container["ImagePullPolicy"] = "IfNotPresent"
    container["image"] = image.strip().replace('"', '')
    containers.append(container)
    idx += 1
pod["spec"]["containers"] = containers
print(yaml.dump(pod))