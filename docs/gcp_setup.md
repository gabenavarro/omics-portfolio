
# GCP Setup

### Prerequisite

1. Access to Google Cloud Artifact Registry. Location where docker images are deposited in order to GCP to create transient containers during pipeline run.

Install Google Cloud SDK.

```bash
curl https://sdk.cloud.google.com | bash
```
 
After installing, restart shell and initialize GCP credentials.
```bash
gcloud init
```

Lastly, configure docker to have access to GCP project registry. Change location, `us-west1-docker` if your project location is different.
```bash
gcloud auth configure-docker us-west1-docker.pkg.dev
```


### Deployment

To deploy image to GPC artifact registry run the following script.

```bash
bash deploy_image.sh \
     peekaboo-alphafold2-gpu-subprocess:prod \
     us-west1-docker.pkg.dev/ds-development-455369/peekaboo/alphafold2-gpu-subprocess:prod
```


Keep in mind that the official pipeline references the image with the `prod` tag. If you would like to have a test tag, feel free to change the tag to best fit your needs.