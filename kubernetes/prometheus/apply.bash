# Source Environment
. .env

# Automatically dump configmap.yml file and apply
kubectl create configmap --dry-run=client "$CP_CONFIG" \
    --from-file="$CP_CONFIG_PATH" \
    --output yaml \
    > "$CP_CONFIGMAP_PATH"
kubectl apply -f "$CP_CONFIGMAP_PATH"

# Update CONFIG_CHECKSUM annotation to force update config map
export CONFIG_CHECKSUM=$(kubectl get cm/"$CP_CONFIG" -o yaml | sha256sum) && \
cat "$CP_DEPMENT_PATH" | envsubst | kubectl apply -f -

# Update Deployment
kubectl apply -f "$CP_DEPMENT_PATH"