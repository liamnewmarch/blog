---
date: 2020-06-10
title: A web developer’s guide to Google Cloud
summary: An overview to help you decide which service is right for your use case.
image:
  url: /posts/img/web-developers-guide-to-google-cloud.avif
  width: 1554
  height: 1036
---

At Potato we proudly use [Google Cloud](https://cloud.google.com/) services to host our projects (except in cases where a client has a preference for another cloud provider) and have used [App Engine](https://cloud.google.com/appengine/) since the beginning. This has had numerous benefits for us as a business, not least in the current [remote working](https://dev.p.ota.to/post/how-potato-code-remotely-4q64vuq2wb5/) climate.

Our use of cloud services has allowed Potato’s engineers to focus on application development instead of maintaining servers. We can leave platform security and reliability in the hands of some of the best engineers in the world at Google, and at the same time take advantage of world-class availability, scalability and performance.

As with other cloud platforms, Google Cloud has a range of different services to help build and host web applications. At first glance the subtle differences between these services might not be apparent until you start using them, so I’ve put together this guide to give an overview of each service and to help you decide which is right for your use case.

We're going to look at Cloud Storage, Cloud Functions, App Engine, Cloud Run, Cloud Build and Kubernetes Engine. These services broadly come under the category of [serverless](https://en.wikipedia.org/wiki/Serverless_computing) architecture. I won’t go into exactly what it means here, for more information check out the [Serverless computing](https://cloud.google.com/serverless) section of the Google Cloud documentation. We’ll also cover containers, which are described in [this Containers guide](https://cloud.google.com/containers).

## Static hosting with Cloud Storage

[Cloud Storage](https://cloud.google.com/storage/) is an object store used to save files in buckets for later retrieval. A typical use case might be that an App Engine app uses Cloud Storage to save and read user-uploaded files. It’s also possible to [serve a static site](https://cloud.google.com/storage/docs/hosting-static-website) directly from a Cloud Storage bucket with no server code using the [gsutil command line tool](https://cloud.google.com/storage/docs/gsutil), or the Google Cloud web interface.

This approach takes advantage of [Google's CDN](https://cloud.google.com/cdn/) to serve content at incredible speed, and unlike other solutions below doesn’t suffer from cold start warm-up time. The key disadvantage is that static hosting doesn’t allow for server side programming, however Cloud Storage can easily be used in conjunction with other services (e.g. [App Engine](https://cloud.google.com/appengine/docs/standard/python/getting-started/serving-static-files)) so it’s very useful to bear in mind.

*__Useful for:__ static marketing pages; [SPAs](https://en.wikipedia.org/wiki/Single-page_application "Single-page applications") or [PWAs](https://en.wikipedia.org/wiki/Progressive_web_application "Progressive web applications") with no back-end requirement.*

## Serverless functions with Cloud Functions

[Cloud Functions](https://cloud.google.com/functions/) are a lightweight alternative to running full back-end applications on App Engine or Cloud Run, and are ideal for use alongside statically served websites or in non-traditional UI contexts such as voice or chat.

Functions can be written in Go, Node.js or Python and are triggered by URL or an event such as when a file is uploaded to storage or when commits are pushed to a Git branch. Analogous to functional programming, Cloud Functions are designed to be stateless and to accomplish one task; multiple functions can be defined to break up complex or concurrent tasks. This makes functions powerful but will likely require substantial refactoring of complex apps.

It’s also worth noting that functions can scale with demand, but the first request after a period of inactivity may be slower because functions will automatically be put in a low resource state. This is known as a cold start.

*__Useful for:__ lightweight APIs written with [Flask](https://flask.palletsprojects.com/) or [Express.js](https://expressjs.com/); event-driven data processing e.g. image resizing; sending notifications with [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/) or email; chatbots and voice apps that fetch data from a third party API.*

## Serverless applications with App Engine

[App Engine](https://cloud.google.com/appengine) is Google’s cloud service for running sandboxed serverless apps. It comes in two flavours, standard and flexible; each has its own pros and cons but both offer powerful scaling to meet traffic demand.

### Standard environment

[App Engine standard](https://cloud.google.com/appengine/docs/standard) powers the majority of projects at Potato. It supports applications written in Go, Java, Node.js, PHP, Ruby, and – our favourite – Python. App Engine apps make use of URL handlers defined in YAML to route traffic to different parts of the application. Because App Engine is scalable, new instances can spin up to handle increased demand in traffic.

Standard instances can also ‘scale to zero’ when there is no demand which can helpful in reducing billing costs. For this reason it’s important to be mindful of statelessness, similar to Cloud Functions. Unlike Cloud Functions however, App Engine is designed to accommodate complex applications and [several ‘instance classes’ are available](https://cloud.google.com/appengine/docs/standard#instance_classes) with different memory and CPU constraints.

*__Useful for:__ traditional server-based web applications such as those built with frameworks like [Symfony](https://symfony.com/) (PHP) and [Django](https://www.djangoproject.com/) (Python).*

### Flexible environment

[App Engine flex](https://cloud.google.com/appengine/docs/flexible) allows you to use custom runtimes as well as those found in App Engine standard. Custom runtimes use [Docker](https://www.docker.com/) which allows you to run custom server code in a sandboxed container. Many predefined container images can be found on [Docker Hub](https://hub.docker.com/) and in [Google Container Registry](https://cloud.google.com/container-registry/).

App Engine flex apps can scale with traffic like standard apps, but they cannot scale to zero. This means apps only need to warm up when starting new instances since there is no cold start from zero, but also means apps will incur billing costs while idle. For this reason flex is less suitable for infrequently-used or hobby projects.

*__Useful for:__ traditional server-based web applications on custom runtimes e.g. [.NET](https://dotnet.microsoft.com/), [Deno](https://deno.land/) (make sure to read our [An Introduction to Deno](https://dev.p.ota.to/post/an-introduction-to-deno-4u3suut77w6/) post next!)*

## Application containers with Cloud Run

If you need more flexibility over your runtime environment than App Engine standard allows, consider using [Cloud Run](https://cloud.google.com/run/) over App Engine flexible. Cloud Run is a recent addition to the Google Cloud family which runs containers [natively](https://cloud.google.com/knative/) on [Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) rather than in a [Compute Engine](https://cloud.google.com/compute/) virtual machine like App Engine.

Apart from faster warm up speed compared to App Engine flex, Cloud Run also has App Engine standard’s ability to scale the number of active instances to zero when not in use. This can be helpful in reducing billing costs.

*__Useful for:__ traditional server-based web applications on any runtime; [Symfony](https://symfony.com/) (PHP), [Django](https://www.djangoproject.com/) (Python), [.NET](https://dotnet.microsoft.com/), [Deno](https://deno.land).*

## CI/CD containers with Cloud Build

[Cloud Build](https://cloud.google.com/cloud-build/) is not a service that can respond directly to HTTP requests but deserves an honourable mention because of how it fits into the Google Cloud serverless family. In many ways it’s a continuation of the event driven invocation model seen in Cloud Functions; builds are triggered by a linked Git repository (either a [Cloud Source Repository](https://cloud.google.com/source-repositories/), [Bitbucket](https://bitbucket.org/product/) or [GitHub](https://github.com/)).

Builds follow a step-by-step list of procedures that run in containers. This allows you to automatically run [CI/CD](https://en.wikipedia.org/wiki/CI/CD) tasks such as compilation, testing, and deployment to App Engine or Cloud Run, all by pushing commits or tags to a Git branch.

*__Useful for:__ unit testing; end-to-end testing; compiling assets; deploying to App Engine, Cloud Run or Kubernetes Engine.*

## Container clusters with Kubernetes Engine

The last service I want to talk about is [Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) which is used for orchestrating multiple containers. As mentioned above, Cloud Run itself runs on Kubernetes Engine.

If you find that your application architecture has become sufficiently complex that you need more control over multiple microservice containers, or dynamic load balancing between different versions of your app, then this may be the solution for you. The obvious drawback is that you need to configure this architecture yourself and thus it requires more specialist DevOps knowledge. Also bear in mind that it’s possible to run multiple instances of Cloud Run or App Engine in the same project and this covers most complex use cases.

*__Useful for:__ complex application architectures; multi/microservice apps; orchestrating multiple runtimes as a single managed service.*

## Summary

The service that's right for you really depends on the complexity of your application.

- If your application has a dynamic back-end and is written in Go, Java, Node.js, PHP, Python or Ruby, use **App Engine standard**.
- If your application has a dynamic back-end but is written in a language or version unsupported by App Engine use **Cloud Run**.
-  If your application has a complex back-end which uses multiple runtimes or a microservice architecture consider multiple **Cloud Run** services or **Kubernetes Engine**.
-  If your application has no dynamic back-end consider using **App Engine standard** to [serve static files](https://cloud.google.com/appengine/docs/standard/python/getting-started/serving-static-files) or a dedicated static hosting service such as [Firebase Hosting](https://firebase.google.com/products/hosting) or [GitHub Pages](https://pages.github.com).
-  If your application doesn’t need a web front-end and only requires minimal stateless processing use **Cloud Functions**.
