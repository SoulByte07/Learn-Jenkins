FROM jenkins/jenkins:lts
USER root

# Install buildah and fuse-overlayfs
RUN apt-get update && apt-get install -y buildah fuse-overlayfs

# Jenkins runs as root in this setup; allow git operations in mounted workspaces
RUN git config --system --add safe.directory '*'

# Create the subuid/subgid files so buildah can map IDs correctly
RUN echo "jenkins:100000:65536" > /etc/subuid && \
    echo "jenkins:100000:65536" > /etc/subgid

# Buildah configuration for rootless mode inside a container
RUN mkdir -p /home/jenkins/.config/containers
RUN echo "[storage]\ndriver = \"vfs\"" > /home/jenkins/.config/containers/storage.conf

RUN chown -R jenkins:jenkins /home/jenkins/.config

# Run Jenkins process as root in this nested-container setup so Buildah
# can avoid rootless user namespace mapping failures.
USER root
