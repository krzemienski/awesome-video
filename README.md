# Awesome Video [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
 
<!-- 

PLEASE DO NOT UPDATE THIS FILE, UPDATE CONTENTS.JSON INSTEAD. THANK YOU :-)

 -->





### Contents

- [Introduction](#introduction)
- [Learning](#learning)
  - [Books](#books)
  - [Reading](#reading)
  - [Talks Presentations Podcasts](#talks-presentations-podcasts)
- [HLS](#hls)
- [DASH](#dash)
- [Kubernetes](#kubernetes)
- [Encoding](#encoding)
  - [AV1](#av1)
  - [HEVC](#hevc)
  - [VP9](#vp9)
- [Transport](#transport)
  - [RIST](#rist)
  - [RTMP](#rtmp)
  - [SRT](#srt)
- [Streaming Server and Storage](#streaming-server-and-storage)
- [Specs and Standards](#specs-and-standards)
  - [Industry Forums](#industry-forums)
  - [MPEG](#mpeg)
- [Players](#players)
  - [Android](#android)
  - [Chromecast](#chromecast)
  - [iOS tvOS](#ios-tvos)
  - [Roku](#roku)
  - [Smart TVs](#smart-tv)
  - [Web](#web)
- [FFMPEG](#ffmpeg)
- [Audio](#audio)
- [Subtitles and Captions](#subtitles-and-captions)
- [Dubbing](#dubbing)
- [Ads](#ads)
- [Vendors](#vendors)
  - [Dolby](#dolby)
- [QoE](#qoe)
- [Tools](#tools)
- [DRM](#drm)
- [Testing](#testing)
- [Community](#community)
  - [Conferences](#conferences)
  - [Meet ups](#meetups)
  - [Slack Groups](#slack)
- [CDN](#cdn)
- [HDR10, HLG, Dolby Vision](#hdr)

## Introduction
*What's video?*

* [A short history of video coding](https://www.slideshare.net/vcodex/a-short-history-of-video-coding?from_m_app=ios)  - Video coding is an essential component of video streaming, digital TV, video chat and many other technologies. This presentation, an invited lecture to the US …
* [Eyevinn/streaming-onboarding](https://github.com/Eyevinn/streaming-onboarding)  - New to streaming and don't know where to start? This is the place for you! - Eyevinn/streaming-onboarding
* [Video Streaming Cheatsheet](https://video-streaming-cheatsheet.s3.eu-west-2.amazonaws.com/artifacts/video-streaming-cheatsheet.pdf)  - The Video Streaming Cheatsheet is a double sided page, suitable for printing, that contains common terminology used in the video streaming industry in a quick reference format
* [leandromoreira/digital_video_introduction](https://github.com/leandromoreira/digital_video_introduction)  - A hands-on introduction to video technology: image, video, codec (av1, vp9, h265) and more (ffmpeg encoding). - leandromoreira/digital_video_introduction

## Learning
*An awesome list of learning video streaming resources.*

* [3 Cases from a Video Expert: Encoding Basics](https://link.medium.com/z6IDbLDWO7)  - Introduction
* [Back to Basics: Encoding Definition and Adaptive Bitrate](https://bitmovin.com/encoding-definition-bitrates/?utm_campaign=Newsletter&utm_medium=email&_hsenc=p2ANqtz-8MPFxhR7snQrxPYM7Bl3UTEMgOh5ZXoDQCHjLl9lkskqE0IfBhEuz3us39Br-lvA_CnyNmQl6L5wqO6iKOfAJ8HznenQ&_hsmi=79678208&utm_content=79677632&utm_source=hs_email&hsCtaTracking=b8eb0e0a-f292-435e-8b99-719b75d81412%7C367afa65-d810-4c2e-aa2c-c87e897a8942)  - 
* [Creating A Production Ready Multi Bitrate HLS VOD stream - Peer5 P2P Docs](https://docs.peer5.com/guides/production-ready-hls-vod/)  - Peer5 documentation
* [Creating a Master Playlist | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/creating_a_master_playlist#overview)  - 
* [FFmpeg and how to use it wrong](https://videoblerg.wordpress.com/2017/11/10/ffmpeg-and-how-to-use-it-wrong/)  - I’ve been in the streaming media industry since 2008 and have seen a lot of misinformation regarding both FFmpeg and libx264. In this post I hope to help shed some light on what does and does…
* [Guide to Mobile Video Streaming with HLS](https://mux.com/blog/mobile-hls-guide/)  - HTTP Live Streaming, also known as HLS, is the most common format used today for streaming video. If you're building a video streaming application today, you should probably use HLS. Apple created the HLS standard in 2009, and it is the required streaming format for iOS devices. Since then, Android
* [HLS Authoring Specification for Apple Devices | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/hls_authoring_specification_for_apple_devices)  - 
* [HLS adaptive streaming tutorial with CloudFront & JW Player | Miracle Tutorials](https://www.miracletutorials.com/hls-adaptive-streaming-tutorial-with-cloudfront-jw-player/)  - A step-by-step HLS adaptive streaming tutorial with CloudFront & JW Player in two parts. It is easier than you think. This tutorial presumes you have
* [HOW TO: View an HLS Stream in QuickTime or VLC – Softron Support Desk](https://softron.zendesk.com/hc/en-us/articles/207694617-HOW-TO-View-an-HLS-Stream-in-QuickTime-or-VLC?mobile_site=true)  - 
* [How To Setup Nginx For HLS Video Streaming On Centos 7](https://dev.to/samuyi/how-to-setup-nginx-for-hls-video-streaming-on-centos-7-3jb8)  - How to live stream videos with Nginx
* [How video streaming works on the web: An introduction](https://medium.com/canal-tech/how-video-streaming-works-on-the-web-an-introduction-7919739f7e1)  - Note: this article is an introduction to video streaming in JavaScript and is mostly targeted to web developers. A large part of the…
* [HowVideo.works](https://howvideo.works)  - 
* [Internet Video Streaming — ABR part 1](https://medium.com/@eyevinntechnology/internet-video-streaming-abr-part-1-b10964849e19?source=userActivityShare-94bccb50d11-1559723768&_branch_match_id=664736558865703297)  - Background
* [Internet Video Streaming — ABR part 2](https://medium.com/@eyevinntechnology/internet-video-streaming-abr-part-2-dbce136b0d7c?source=userActivityShare-94bccb50d11-1559723862&_branch_match_id=664736952377004405)  - Background
* [Introduction to HTTP Live Streaming: HLS on Android and More](https://www.toptal.com/apple/introduction-to-http-live-streaming-hls)  - This article explains how HTTP Live Streaming works and demonstrates how to create an HLS player in Android.
* [Low Latency Live Streaming](https://docs.google.com/presentation/d/1ZwqWcweR5SqeMBRmJjSukWaHbpdPy-EPYvJCS23_n3U/edit?usp=sharing)  - Low Latency Live Streaming Apple LLHLS / CMAF Kevin Staunton-Lambert Solutions Architect R&D (July 2019) @kevleyski www.switch.tv
* [OTT Content Delivery](https://medium.com/@eyevinntechnology/ott-content-delivery-b43a35ef24f6)  - Background
* [OTT Content Delivery– Multi CDN](https://medium.com/@eyevinntechnology/ott-content-delivery-multi-cdn-8cd90ad2628a?source=userActivityShare-94bccb50d11-1560983307&_branch_match_id=670019455010399744)  - Background
* [Overview of the H.264/AVC video coding standard - Circuits and Systems for Video Technology, IEEE Transactions on](http://ip.hhi.de/imagecom_G1/assets/pdfs/csvt_overview_0305.pdf)  - 
* [Server-less Video Backend](https://medium.com/@eyevinntechnology/server-less-video-backend-1a142d1d2ba)  - In this blog post by Jonas Rydholm Birmé he describes how a completely server-less video backend on AWS would look like.
* [The structure of an MPEG-DASH MPD](https://www.brendanlong.com/the-structure-of-an-mpeg-dash-mpd.html)  - The MPEG-DASH Media Presentation Description (MPD) is an XML document containing information about media segments, their relationships and information necessary to choose between them, and other metadata that may be needed by clients. In this post, I describe the most important pieces of the MPD, starting from the top level (Periods) and going to the bottom (Segments).
* [Understanding the HTTP Live Streaming Architecture | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/understanding_the_http_live_streaming_architecture)  - 
* [VOD2Live](https://docs.google.com/presentation/d/1Ua76BBaZKtTmaZrlfM_eG0vwz0ZAqPIjreCSfB4qFQQ/edit?usp=sharing)  - VOD2Live Kevin Staunton-Lambert Solutions Architect R&D @kevleyski www.switch.tv
* [Video Encoding — Compression and Resolutions](https://medium.com/@eyevinntechnology/chessboard-for-beginners-video-encoding-compression-and-resolutions-bcefe04fa639)  - Written by: Boris Asadanin, Streaming Media Consultant at Eyevinn Technology
* [Video Tensorflow](https://docs.google.com/presentation/d/1NAqYWmFOwxJEacZCuPLdX0mRNRFPFgeRbsm22EaxerU/edit?usp=sharing)  - Using Tensorflow For Audience Measurement Kevin Staunton-Lambert Solutions Architect R&D @kevleyski www.switch.tv
* [Video and containers](http://neurocline.github.io/dev/2016/07/28/video-and-containers.html)  - NALU, Annex B, and Start Codes
* [WebAssembly (Wasm)](https://docs.google.com/presentation/d/1sonEk2neNVBcy8EzieUjWCNzj5SXN7dk-unkR_lpl8k/edit?usp=sharing)  - WebAssembly (Wasm) On the Edge Kevin Staunton-Lambert Solutions Architect R&D @kevleyski www.switch.tv Wasm)
* [WildFires](https://docs.google.com/presentation/d/1yiVEOq2rvtFynP1tLdJj7pBWkAEiE9g8BMaoryxRVrk/edit?usp=sharing)  - VOD2Live Kevin Staunton-Lambert Solutions Architect R&D @kevleyski Wild Fire! How video engineers can help save lives www.switch.tv
* [alexgand/springer_free_books: Python script to download all Springer books released for free during the 2020 COVID-19 quarantine](https://github.com/alexgand/springer_free_books)  - Python script to download all Springer books released for free during the 2020 COVID-19 quarantine - alexgand/springer_free_books
* [amiaopensource/cable-bible](https://github.com/amiaopensource/cable-bible)  - A guide to cables and connectors used for audiovisual tech - amiaopensource/cable-bible
* [bash scripts to create VOD HLS stream with ffmpeg almighty (tested on Linux and OS X)](https://gist.github.com/mrbar42/ae111731906f958b396f30906004b3fa)  - bash scripts to create VOD HLS stream with ffmpeg almighty (tested on Linux and OS X) - README.md
* [ffmpeg tutorial](http://www.dranger.com/ffmpeg/)  - 
* [leandromoreira/video-containers-debugging-tools](https://github.com/leandromoreira/video-containers-debugging-tools)  - A set of command lines to debug video streaming files like mp4 (MPEG-4 Part 14), ts (MPEG-2 Part 1), fmp4 in Dash, HLS, or MSS, with or without DRM. - leandromoreira/video-containers-debugging-tools
* [lhls-simple-live-platform](https://slides.com/jordicenzano/deck-973aed)  - You can build your own live platform just wiring up some open source tools, this is a demo video of https://github.com/jordicenzano/lhls-simple-live-platform
* [matmoi/create-DASH-HLS](https://github.com/matmoi/create-DASH-HLS/)  - A tutorial to generate fMp4 files compatible with dash and HLS - matmoi/create-DASH-HLS
* [matmoi/create-DASH-HLS](https://github.com/matmoi/create-DASH-HLS)  - A tutorial to generate fMp4 files compatible with dash and HLS - matmoi/create-DASH-HLS
* [mofo7777/Stackoverflow](https://github.com/mofo7777/Stackoverflow)  - All source codes I've provided on stackoverflow as an answer, usually under tag ms-media-foundation. Mediafoundation, audio, video, 3D, decoder, encoder. - mofo7777/Stackoverflow
* [nickdesaulniers/netfix](https://github.com/nickdesaulniers/netfix)  - Let's build a Netflix. 

### Books
*Books on video streaming. NOTE: Books published more than 4-5 years ago may not be up to date on latest streaming tech.*
[back to top](#readme) 

* [Circles of Confusion](https://tech.ebu.ch/publicaions/circles-of-confusion)  - 2009-01-01. Roberts, Alan.
* [Communicating Pictures](https://www.elsevier.com/books/communicating-pictures/bull/978-0-12-405906-1)  - 2014-06-20 (1st Edition). Bull, David.
* [Fundamentals of Multimedia](https://www.amazon.com/Fundamentals-Multimedia-Texts-Computer-Science/dp/303062126X/)  - 2022-02-17 (3rd Edition). Ze-Nian Li (Author), Mark S. Drew (Author), Jiangchuan Liu.
* [The Good Parts of LibVLC](https://mfkl.gumroad.com/l/libvlc-good-parts)  - 2022-09-15. Finkel, Martin.
* [Video Compression Handbook](https://www.amazon.com/dp/0134866215/)  - 2018-07-03 (2nd Edition). Beach, Andy; Owen, Aaron.

### Reading
*A list of reading articles, blogs, and newsletters for video streaming.*
[back to top](#readme) 

* [9 Best Home Server Apps to Automate Media Management](https://www.smarthomebeginner.com/best-home-server-apps/)  - These are top 9 best home server apps to automate media management, so you get the latest Movies, Music and TV Shows in the best quality available.
* [About Frame Rates or Why 29.97?](http://theautomaticfilmmaker.com/blog/2009/2/23/about-frame-rates-or-why-2997.html)  - I recently remembered this popular post from my old blog. Since that blog no longer exists, I thought I would repost it here. Since I wrote this post about a decade ago, many others of done a much better job describing this in detail. I highly recommend the following two videos by Alec Watson fro
* [BOLA: Near-Optimal Bitrate Adaptation for Online Videos](https://arxiv.org/pdf/1601.06748.pdf)  - 
* [Byte Down: Making Netflix’s Data Infrastructure Cost-Effective](https://netflixtechblog.com/byte-down-making-netflixs-data-infrastructure-cost-effective-fee7b3235032)  - 
* [Demystifying HTML5 Video Player](https://medium.com/@eyevinntechnology/demystifying-html5-video-player-e480846328f0)  - In this post we will go under the hood of a HTML video player for video streaming. With the exception of Apple and their browser Safari, no…
* [Design of scheduling and rate-adaptation algorithms for adaptive HTTP streaming · dispar.at Blog](https://dispar.at/blog/2017/07/08/design-of-scheduling-and-rate-adaptation-algorithms-for-adaptive-http-streaming/)  - Design of scheduling and rate-adaptation algorithms for adaptive HTTP streaming - Stephan Hesse
* [Extracting contextual information from video assets](https://medium.com/netflix-techblog/extracting-contextual-information-from-video-assets-ee9da25b6008)  - for an improved Netflix user experience
* [FFmpeg Threads Command: How it Affects Quality and Performance](https://streaminglearningcenter.com/blogs/ffmpeg-command-threads-how-it-affects-quality-and-performance.html)  - So, I received an email from an acquaintance that read, “I was curious if there is actually any benefit to a “threads=” type custom command in x264. Specifically many streamers are buying 8 core/16 thread CPUs to encode as a standalone client capturing information from a video capture device.” I had an article on FFmpeg…
* [HDMI 2.1: features, specs and news about the latest HDMI standard](https://www.whathifi.com/advice/what-hdmi-21-everything-you-need-to-know)  - The gateway to a super high-definition future is ever-nearing
* [Hardware-Assisted Video Transcoding At Dailymotion](https://link.medium.com/jfUev36Zs8)  - What if you could save time, power consumption and therefore money, while still keeping a decent quality for your converted video ?
* [IMF: A Prescription for Versionitis](https://medium.com/netflix-techblog/imf-a-prescription-for-versionitis-e0b4c1865c20)  - the emerging Interoperable Master Format standard
* [Improving our video encodes for legacy devices](https://link.medium.com/T7S5MS6IT8)  - by Mariana Afonso, Anush Moorthy, Liwei Guo, Lishan Zhu, Anne Aaron
* [Inside MPEG's Ambitious Plan to Launch 3 Video Codecs in 2020](https://www.streamingmedia.com/Articles/Editorial/Featured-Articles/Inside-MPEGs-Ambitious-Plan-to-Launch-3-Video-Codecs-in-2020-134694.aspx)  - The pace of innovation is getting faster and the demands on video codecs are getting greater. MPEG's three-part plan answers questions of royalties, licensing, and computational efficiency. Meet VVC, MPEG-5 Part 1 (EVC), and MPEG-5 Part 2 (LCEVC).
* [Live Video Transmuxing/Transcoding: FFmpeg vs TwitchTranscoder, Part I](https://link.medium.com/iws08p9VO7)  - By: Jeff Gong, Software Engineer, jeffgon@twitch.tv Sahil Dhanju, Software Engineer Intern Chih-Chiang Lu, Senior Software Engineer…
* [Live Video Transmuxing/Transcoding: FFmpeg vs TwitchTranscoder, Part II](https://link.medium.com/EYVMBQ3VO7)  - By: Jeff Gong, Software Engineer, jeffgon@twitch.tv Sahil Dhanju, Software Engineer Intern Chih-Chiang Lu, Senior Software Engineer…
* [Quantifying packaging overhead](https://mux.com/blog/quantifying-packaging-overhead-2)  - Mux makes adding video to your app or website as easy as making a single API call. But behind the scenes is a large multistep process to analyze and transform the video into something that can be easily consumed by a device. This process is commonly called a media “pipeline”
* [Riot Games Keeps League of Legends Esports Rolling With Fully Cloud-Based Virtualized Workflow](https://www.sportsvideo.org/2020/03/27/riot-games-keeps-league-of-legends-esports-rolling-with-fully-cloud-based-virtualized-production-workflow/)  - Although the traditional sports world has come to a standstill due to the coronavirus pandemic, many major esports properties are soldiering on, hosting compe
* [Running FFmpeg on AWS Lambda for 1.9% the cost of AWS Elastic Transcoder](https://intoli.com/blog/transcoding-on-aws-lambda/)  - A guide to building a transcoder using Exodus, FFmpeg, and AWS Lambda.
* [Saving on Encoding and Streaming: Deploy Capped CRF – Streaming Learning Center](https://streaminglearningcenter.com/blogs/saving-encoding-streaming-deploy-capped-crf.html)  - This is the second in a five-part series on how to cut your encoding and streaming costs. The first article was Saving on Encoding: Adjust Encoding Configuration to Increase Capacity. Article summary: Capped CRF encoding is a single-pass encoding method that can save encoding costs compared to two-pass VBR. Capped CRF is also a simple per-title…
* [Server-less Just-in-Time Packaging with AWS Fargate and Unified Origin by Unified Streaming](https://medium.com/@eyevinntechnology/server-less-just-in-time-packaging-with-aws-fargate-and-unified-origin-by-unified-streaming-c1682dc051ca?source=userActivityShare-94bccb50d11-1559724204&_branch_match_id=664738392430917730)  - In this blog article Jonas Rydholm Birmé describes how he created a server-less just-in-time packaging origin, using AWS ECS Fargate tasks…
* [Server-less Just-in-Time Packaging with AWS Fargate and Unified Origin by Unified Streaming](https://medium.com/@eyevinntechnology/server-less-just-in-time-packaging-with-aws-fargate-and-unified-origin-by-unified-streaming-c1682dc051ca?source=userActivityShare-94bccb50d11-1560983627&_branch_match_id=670020794794030328)  - In this blog article Jonas Rydholm Birmé describes how he created a server-less just-in-time packaging origin, using AWS ECS Fargate tasks…
* [Streaming Live From the Battlefield: Military Video in 2019](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=135141)  - Metadata and low-latency video create a tactical advantage in intelligence-gathering and decision making. Discover why HEVC is gaining momentum in the armed forces, and Android is preferred over iOS.
* [The H.264 Sequence Parameter Set](https://www.cardinalpeak.com/the-h-264-sequence-parameter-set)  - [vc_row][vc_column][vc_column_text]This is a follow-up to my World’s Smallest H.264 Encoder post. I’ve received several emails asking about precise details of things in two entities in the H.264 bitstream: the Sequence Parameter Set (SPS) and the Picture Parameter Set (PPS). Both entities contain information that an H.264 decoder needs to decode the video data, for example,…
* [The Netflix IMF Workflow](https://medium.com/netflix-techblog/the-netflix-imf-workflow-f45dd72ed700?source=userActivityShare-94bccb50d11-1568773157&_branch_match_id=702692448596112473)  - interesting architectural implications
* [VOD on AWS](https://s3.amazonaws.com/solutions-reference/video-on-demand-on-aws/latest/video-on-demand-on-aws.pdf)  - 
* [Video Coding - BBC R&D](https://www.bbc.co.uk/rd/projects/video-coding)  - BBC video encoding R&D home page
* [Video in the War Zone: The Current State of Military Streaming](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=101310)  - For the armed forces, streaming is a matter of national security. Here's an exclusive look at how the military, from analysts to ground troops, is using streaming video.
* [Video: HLS and DASH Multi-Codec Encoding & Packaging](https://thebroadcastknowledge.com/2020/07/10/video-hls-and-dash-multi-codec-encoding-packaging/)  - Free educational webinars, videos and other resources focused on the Broadcast Industry

### Talks Presentations Podcasts
*Conference talks and pdf presentations and podcasts on streaming video .*
[back to top](#readme) 

* [Demuxed 2016](https://www.youtube.com/watch?v=kEo2TrXm7F4&list=PLkyaYNWEKcOekC2m9Na77G40Lmhb1bnsK)  - 2016 Demuxed talks & presentations
* [Demuxed 2017](https://www.youtube.com/watch?v=PSdhW-R9u6s&list=PLkyaYNWEKcOfntbMd6KtHhF7qpL9hj6of)  - 2017 Demuxed talks & presentations
* [Demuxed 2018](https://www.youtube.com/watch?v=bfK_f7GBA8s&list=PLkyaYNWEKcOfARqEht42i1P4kBemzEV2V)  - 2018  Demuxed talks & presentations
* [Demuxed 2019](https://m.youtube.com/playlist?list=PLkyaYNWEKcOf_C_6W45abNvXMb40xUUqh)  - 2019 Demuxed talks & presentations
* [Demuxed 2020](https://www.youtube.com/playlist?list=PLkyaYNWEKcOcDlGjEbpxBe4woCJGHrarN)  - 2020 Demuxed talks & presentations
* [Demuxed 2021](https://www.youtube.com/playlist?list=PLkyaYNWEKcOfD1GYFxFbZXDP03XM-cZPg)  - 2021 Demuxed talks & presentations
* [Demuxed 2022](https://www.youtube.com/playlist?list=PLkyaYNWEKcOf98lZxnCcL6y7ZIVU3oSYO)  - 2022 Demuxed talks & presentations
* [Demuxed | Heavybit](https://www.heavybit.com/library/podcasts/demuxed)  - Demuxed is a podcast made for and by engineers working with video. Brought to you by Heavybit.
* [From Sys Admin to Netflix SRE](https://www.youtube.com/watch?v=lZI51YzIgVE)  - Talk by Jonah Horowitz, Albert Tobey What does it take to be a Netflix SRE? With tens of thousands of Linux instances in a distributed system architecture, a...
* [Mile High Video 2018 Proceedings](https://mile-high.video/files/mhv2018)  - Mile High Video 2018 talks & presentations
* [Mile High Video 2019 Proceedings](https://mile-high.video/files/mhv2019)  - Mile High Video 2019 talks & presentations
* [The Video Insiders](https://thevideoinsiders.simplecast.com/episodes)  - Video Insiders Podcast
* [Video Coding Basics - How is this so efficient?](https://youtu.be/LDeL7-49qm4)  - An introduction to the basics of video coding

## HLS
*HLS tools, libraries, and resources.*

* [507_hls_authoring_for_airplay_2.](https://devstreaming-cdn.apple.com/videos/wwdc/2019/507fk9wyls0np6piwk/507/507_hls_authoring_for_airplay_2_video.pdf)  - 
* [510_validating_http_live_streams.](https://devstreaming-cdn.apple.com/videos/wwdc/2016/510ndmh9wkcvzneegv2/510/510_validating_http_live_streams.pdf)  - 
* [Eyevinn/hls-cutsegment](https://github.com/Eyevinn/hls-cutsegment)  - A web app that lets you insert a cut into a segment, which is then cut into two new segments. - Eyevinn/hls-cutsegment
* [Eyevinn/hls-download](https://github.com/Eyevinn/hls-download)  - Download HLS and convert to MP4.
* [Eyevinn/hls-origin-scripts](https://github.com/Eyevinn/hls-origin-scripts)  - Scripts to manipulate HLS manifests at origin or edge server - Eyevinn/hls-origin-scripts
* [Eyevinn/hls-playlist-parser](https://github.com/Eyevinn/hls-playlist-parser)  - A Javascript library to parse Hls playlists.
* [Eyevinn/hls-relay](https://github.com/Eyevinn/hls-relay)  - Script to pull HLS stream from one origin and push to another origin - Eyevinn/hls-relay
* [Eyevinn/hls-ts-analyzer](https://github.com/Eyevinn/hls-ts-analyzer)  - Example implementation of hls-ts.js library. 
* [Eyevinn/hls-ts-js](https://github.com/Eyevinn/hls-ts-js)  - HLS MPEG-TS parser library in Javascript.
* [Eyevinn/manifestparser](https://github.com/Eyevinn/manifestparser)  - A manifest parser.
* [Eyevinn/vod-to-live](https://github.com/Eyevinn/vod-to-live)  - A python library to generate Live HLS from VOD.
* [HLS and Fragmented MP4](https://hlsbook.net/hls-fragmented-mp4/)  - At WWDC 2016, Apple announced support for fragmented MP4 (fMP4) as an alternative to MPEG-TS, which prior to their announcement was the only supported format. So why use fragmented MP4 files? Well,…
* [HLS | Bento4](https://www.bento4.com/developers/hls/)  - 
* [Integrating AirPlay for Long-Form Video Apps | Apple Developer Documentation](https://developer.apple.com/documentation/avfoundation/airplay_2/integrating_airplay_for_long-form_video_apps)  - 
* [Introducing Low-Latency HLS - WWDC 2019 - Videos - Apple Developer](https://developer.apple.com/videos/play/wwdc2019/502)  - Since its introduction in 2009, HTTP Live Streaming (HLS) has enabled the delivery of countless live and on‐demand audio and video...
* [Last-Order/Minyami](https://github.com/Last-Order/Minyami)  - A lovely video downloader for HLS videos.
* [M3U8Kit/M3U8Parser](https://github.com/M3U8Kit/M3U8Parser)  - A light weight M3U8 parser. Support X-Key & X-Session-Key. - M3U8Kit/M3U8Parser
* [Protocol Extension for Low-Latency HLS (Preliminary Specification) | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/protocol_extension_for_low-latency_hls_preliminary_specification#3291001)  - 
* [SoulMelody/hls-get](https://github.com/SoulMelody/hls-get)  - An asynchronous terminal-based hls video stream (m3u8) downloader & combiner, with AES-128 decryption support. - SoulMelody/hls-get
* [alfg/docker-nginx-rtmp](https://github.com/alfg/docker-nginx-rtmp)  - 🐋 A Dockerfile for nginx-rtmp-module + FFmpeg from source with basic settings for streaming HLS. Built on Alpine Linux. - alfg/docker-nginx-rtmp
* [carlanton/m3u8-parser](https://github.com/carlanton/m3u8-parser)  - HLS compliant m3u8 parser for Java.
* [cdnbye/hlsjs-p2p-engine](https://github.com/cdnbye/hlsjs-p2p-engine)  - A hls.js plugin to offload bandwidth from expensive traditional CDNs，while also maximizing a user’s viewing experience.  - cdnbye/hlsjs-p2p-engine
* [creeveliu/HTTPLiveStreamingTools](https://github.com/creeveliu/HTTPLiveStreamingTools)  - Latest Apple HLS tools copy from Apple Developer Center - creeveliu/HTTPLiveStreamingTools
* [denex/hls-downloader](https://github.com/denex/hls-downloader)  - Download all video files from HLS (HTTP Live Streaming) VoD (Video on Demand) m3u8 playlist for local playback - denex/hls-downloader
* [dhairav/URLSessionHLSDownload](https://github.com/dhairav/URLSessionHLSDownload)  - A swift 3 implementation for downloading HLS content and play it back using native AVPlayer - dhairav/URLSessionHLSDownload
* [epiclabs-io/hls-analyzer](https://github.com/epiclabs-io/hls-analyzer)  - Analyzer for HTTP Live Streams (HLS) content.
* [fcanas/HLSCore](https://github.com/fcanas/HLSCore)  - A collection of Swift packages for working with HLS - fcanas/HLSCore
* [flavioribeiro/nginx-audio-track-for-hls-module](https://github.com/flavioribeiro/nginx-audio-track-for-hls-module)  - :sound: Nginx module that generates audio track for HTTP Live Streaming (HLS) streams on the fly. - flavioribeiro/nginx-audio-track-for-hls-module
* [flavioribeiro/nginx-vod-module-fmp4-hls](https://github.com/flavioribeiro/nginx-vod-module-fmp4-hls)  - Play fragmented mp4's on HLS using nginx-vod-module - flavioribeiro/nginx-vod-module-fmp4-hls
* [globocom/hlsclient](https://github.com/globocom/hlsclient)  - Python HLS Client.
* [globocom/m3u8](https://github.com/globocom/m3u8)  - M3U8 library
* [grafov/m3u8](https://github.com/grafov/m3u8)  - Parser and generator of M3U8-playlists for Apple HLS. Library for Go language. :cinema: - grafov/m3u8
* [iheartradio/open-m3u8](https://github.com/iheartradio/open-m3u8)  - Open Source m3u8 Parser.
* [iliya-gr/mediasegmenter](https://github.com/iliya-gr/mediasegmenter)  - HLS media segmenter.
* [imsanthosh/HLS-Stream-health-monitoring-tool](https://github.com/imsanthosh/HLS-Stream-health-monitoring-tool)  - HLS stream health monitoring utility tool provides an report of live HLS stream. This utility tool checks the all available bitrate streams and generates the report in html file format. HTML file i...
* [krad/morsel](https://github.com/krad/morsel)  - 📇 Swift library for creating HLS playlists and fragmented mp4 files.  Works on Linux and iOS. - krad/morsel
* [lcy0321/m3u8-downloader](https://github.com/lcy0321/m3u8-downloader)  - Download the ts files according to the given m3u8 file. - lcy0321/m3u8-downloader
* [leandromoreira/http-video-streaming-troubleshooting](https://github.com/leandromoreira/http-video-streaming-troubleshooting)  - A collection of fixes / problem solutions to HTTP video streaming - leandromoreira/http-video-streaming-troubleshooting
* [majamee/arch-ffmpeg-gpac](https://github.com/majamee/arch-ffmpeg-gpac)  - A ready-prepared video transcoding pipeline to create DASH/ HLS compatible video files & playlists - majamee/arch-ffmpeg-gpac
* [mifi/hls-vod](https://github.com/mifi/hls-vod)  - HTTP Live Streaming with on-the-fly encoding of any video file for Web/Apple TV/iPhone/iPad/iPod - mifi/hls-vod
* [muxinc/hlstools](https://github.com/muxinc/hlstools)  - 
* [nmrony/hlsdownloader](https://github.com/nmrony/hlsdownloader)  - Downloads HLS Playlist file and TS chunks.
* [nmrony/hlsdownloader-cli](https://github.com/nmrony/hlsdownloader-cli)  - Downloads HLS Playlist file and TS chunks using Terminal - nmrony/hlsdownloader-cli
* [openHPI/nginx-hls-analyzer](https://github.com/openHPI/nginx-hls-analyzer)  - Fork of fmsloganalyzer to adapt it for HLS streaming analyzes with nginx - openHPI/nginx-hls-analyzer
* [osklil/hls-fetch](https://github.com/osklil/hls-fetch)  - Download and decrypt videos served by the HTTP Live Streaming (HLS) protocol. - osklil/hls-fetch
* [puemos/hls-downloader-chrome-extension](https://github.com/puemos/hls-downloader-chrome-extension)  - Google Chrome Extension for sniffing and downloading HTTP Live streams (HLS) - puemos/hls-downloader-chrome-extension
* [qi-shun-wang/HLSDownloader](https://github.com/qi-shun-wang/HLSDownloader)  - Download Crypted HLS with server key and play video as local playing on iOS device. - qi-shun-wang/HLSDownloader
* [r-plus/HLSion](https://github.com/r-plus/HLSion)  - HTTP Live Streaming (HLS) download manager to offline playback. - r-plus/HLSion
* [rounce/nginx-hls-module](https://github.com/rounce/nginx-hls-module)  - Smooth Streaming Module fork. 
* [selsta/hlsdl](https://github.com/selsta/hlsdl)  - C program to download VoD HLS (.m3u8) files.
* [shimberger/gohls](https://github.com/shimberger/gohls)  - A server that exposes a directory for video streaming via web interface - shimberger/gohls
* [shrimpgo/video-downloader](https://github.com/shrimpgo/video-downloader)  - Helper to download HLS videos.
* [soldiermoth/hlsq](https://github.com/soldiermoth/hlsq)  - A CLI for adding some color to your HLS manifests along with some basic filtering
* [t-mullen/hls-server](https://github.com/t-mullen/hls-server)  - Middleware for serving HTTP Live Streaming (HLS) compatible media streams. - t-mullen/hls-server
* [tjenkinson/mock-hls-server](https://github.com/tjenkinson/mock-hls-server)  - Fake a live/event HLS stream from a VOD one. Useful for testing. - tjenkinson/mock-hls-server
* [tozastation/HLS-Streaming](https://github.com/tozastation/HLS-Streaming)  - HLSを使ってみたです．. 
* [videojs/m3u8-parser](https://github.com/videojs/m3u8-parser)  - An m3u8 parser.
* [yuhuili-lab/Tide](https://github.com/yuhuili-lab/Tide)  - Simple m3u8 and MPEG-DASH MPD video downloader using libcurl - yuhuili-lab/Tide
* [zhaiweiwei/nginx-hls](https://github.com/zhaiweiwei/nginx-hls)  - Contribute to zhaiweiwei/nginx-hls development by creating an account on GitHub.

## DASH
*DASH tools, libraries, and resources.*

* [DASH IF Test Assets Database](https://testassets.dashif.org/#testcase/details/58a5ddaa7459f8cb201b8a6d)  - 
* [DASH IF Test Assets Database](https://testassets.dashif.org/#testvector/groupedList)  - 
* [DASH Industry Forum | Catalyzing the adoption of MPEG-DASH](https://dashif.org/identifiers/content_protection/)  - 
* [DASH-IF Live Media Ingest Protocol](https://dashif-documents.azurewebsites.net/Ingest/master/DASH-IF-Ingest.pdf)  - 
* [Dash-Industry-Forum/DASH-IF-Conformance](https://github.com/Dash-Industry-Forum/DASH-IF-Conformance)  - This repository provides the source code for MPEG-DASH/DASH-IF Conformance Software/Validator. It has been extended according to further standards, such as CMAF, DVB-DASH, HbbTV, and CTA WAVE. - Da...
* [Dash-Industry-Forum/ISOSegmentValidator](https://github.com/Dash-Industry-Forum/ISOSegmentValidator)  - Contribute to Dash-Industry-Forum/ISOSegmentValidator development by creating an account on GitHub.
* [Dash-Industry-Forum/Ingest](https://github.com/Dash-Industry-Forum/Ingest)  - 
* [Dash-Industry-Forum/dash-live-source-simulator](https://github.com/Dash-Industry-Forum/dash-live-source-simulator)  - DASH live source simulator providing reference live content. - Dash-Industry-Forum/dash-live-source-simulator
* [Dash-Industry-Forum/dash.js](https://github.com/Dash-Industry-Forum/dash.js)  - A reference client implementation for the playback of MPEG DASH via Javascript and compliant browsers. - Dash-Industry-Forum/dash.js
* [Dash-Industry-Forum/media-tools](https://github.com/Dash-Industry-Forum/media-tools)  - A collection of tools for analyzing, handling, and creating media and media containers - Dash-Industry-Forum/media-tools
* [Eyevinn/dash-validator-js](https://github.com/Eyevinn/dash-validator-js)  - MPEG DASH validator JS library. 
* [Eyevinn/docker-2dash](https://github.com/Eyevinn/docker-2dash)  - A Docker container to pre-package MPEG DASH on demand content - Eyevinn/docker-2dash
* [Eyevinn/docker-dash-packager](https://github.com/Eyevinn/docker-dash-packager)  - Open source MPEG DASH packager for live and VOD.
* [Eyevinn/vp9-dash](https://github.com/Eyevinn/vp9-dash)  - FFMpeg wrapper script to create VP9 MPEG-DASH packages - Eyevinn/vp9-dash
* [Guidelines for Implementation: DASH-IF Interoperability Points](https://dashif.org/docs/DASH-IF-IOP-v4.3.pdf)  - 
* [Viblast/dash-proxy](https://github.com/Viblast/dash-proxy)  - Easy downloading and mirroring of MPEG-DASH streams - Viblast/dash-proxy
* [bitmovin/libdash](https://github.com/bitmovin/libdash)  - MPEG-DASH Access Library - Official ISO/IEC MPEG-DASH Reference Implementation - bitmovin/libdash
* [carlanton/mpd-tools](https://github.com/carlanton/mpd-tools)  - DASH MPD tools for Java.
* [dash-mpd-rs](https://github.com/emarsden/dash-mpd-rs)  - Rust library for parsing, serializing and downloading media content from a DASH MPD file.
* [dash-validator-js/README.md at master · Eyevinn/dash-validator-js](https://github.com/Eyevinn/dash-validator-js/)  - MPEG DASH validator JS library. Contribute to Eyevinn/dash-validator-js development by creating an account on GitHub.
* [djvergad/dash](https://github.com/djvergad/dash)  - An MPEG/DASH client-server module for simulating rate adaptation mechanisms over HTTP/TCP. - djvergad/dash
* [mahbubcseju/MPEG-DASH-Downloader](https://github.com/mahbubcseju/MPEG-DASH-Downloader)  - Contribute to mahbubcseju/MPEG-DASH-Downloader development by creating an account on GitHub.
* [mp4dash | Bento4](https://www.bento4.com/documentation/mp4dash/)  - 
* [nickdesaulniers/combine-mpd](https://github.com/nickdesaulniers/combine-mpd)  - Combine MPEG DASH MPD manifest files.
* [pokey909/dash_adaptation_simulator](https://github.com/pokey909/dash_adaptation_simulator)  - Simulate bitrate switching algorithms based on real data traces - pokey909/dash_adaptation_simulator
* [sangwonl/python-mpegdash](https://github.com/caststack/python-mpegdash)  - MPEG-DASH MPD(Media Presentation Description) Parser - sangwonl/python-mpegdash
* [stultus/mp4-to-mpegdash-py](https://github.com/stultus/mp4-to-mpegdash-py)  - Python Script to convert a MP4 file into onDemand MPEG-DASH - stultus/mp4-to-mpegdash-py
* [tchakabam/dash-proxy](https://github.com/tchakabam/dash-proxy)  - Experimental MPEG-DASH media gateway - proxy on-the-fly modified MP4 segment metadata - tchakabam/dash-proxy
* [theolampert/dash-server](https://github.com/theolampert/dash-server)  - Small, command-line HTTP/2 file server for serving MPEG-DASH content. - theolampert/dash-server
* [videojs/mpd-parser](https://github.com/videojs/mpd-parser)  - Contribute to videojs/mpd-parser development by creating an account on GitHub.
* [videojs/videojs-contrib-dash](https://github.com/videojs/videojs-contrib-dash)  - Video.js plugin for supporting the MPEG-DASH playback through a video.js player - videojs/videojs-contrib-dash
* [zencoder/go-dash](https://github.com/zencoder/go-dash)  - A Go library for generating MPEG-DASH manifests. 

## Kubernetes
*Reading & resources, relative to the world of kubernetes leveraged for video devs.*


## Encoding
*Encoding tools, libraries, and resources.*

* [A Large-Scale Comparison of x264, x265, and libvpx](https://medium.com/netflix-techblog/a-large-scale-comparison-of-x264-x265-and-libvpx-a-sneak-peek-2e81e88f8b0f)  - a Sneak Peek
* [AK1194/Video-Compression-motion-estimation-block-video-encoder: This repository is about video compression, and more specifically about the motion estimation block (ME block) of a video encoder. It is a research project for developing an efficient motion](https://github.com/AK1194/Video-Compression-motion-estimation-block-video-encoder)  - This repository is about video compression, and more specifically about the motion estimation block (ME block) of a video encoder. It is a research project for developing an efficient motion estima...
* [Bento4 | Fast, Modern Tools and C++ Class Library for all your MP4 and DASH media format needs](https://www.bento4.com/)  - 
* [CRF Guide (Constant Rate Factor in x264, x265 and libvpx)](https://slhck.info/video/2017/02/24/crf-guide.html)  - What is the Constant Rate Factor?
* [ClearSlide/Fantastic-Transcoder](https://github.com/ClearSlide/Fantastic-Transcoder)  - Fantastic transcoder is a video transcoder which utilizes massively parallel compute to achieve ludicrous conversion speeds. - ClearSlide/Fantastic-Transcoder
* [DolbyLaboratories/dlb_mp4demux: The Dolby MP4 streaming demuxer (dlb_mp4demux) is a software implementation of a demuxer of fragmented or unfragmented ISO base media file format (mp4). It supports demuxing of Dolby Digital (AC-3), Dolby Digital Plus (E-AC](https://github.com/DolbyLaboratories/dlb_mp4demux)  - The Dolby MP4 streaming demuxer (dlb_mp4demux) is a software implementation of a demuxer of fragmented or unfragmented ISO base media file format (mp4). It supports demuxing of Dolby Digital (AC-3)...
* [GeoHaber/Video-Transcode](https://github.com/GeoHaber/Video-Transcode)  - ffmpeg H264 H265 HEVC MPEG Video Trans-code Image-Matrix Collage - GeoHaber/Video-Transcode
* [H.264 profiles and levels | Inside & Outside MediaCoder](http://blog.mediacoderhq.com/h264-profiles-and-levels)  - 
* [Introducing SVT-AV1: a scalable open-source AV1 framework](https://medium.com/netflix-techblog/introducing-svt-av1-a-scalable-open-source-av1-framework-c726cce3103a)  - by Andrey Norkin, Joel Sole, Kyle Swanson, Mariana Afonso, Anush Moorthy, Anne Aaron
* [Live Video Transmuxing/Transcoding: FFmpeg vs TwitchTranscoder, Part 2](https://blog.twitch.tv/live-video-transmuxing-transcoding-ffmpeg-vs-twitchtranscoder-part-ii-4973f475f8a3?source=userActivityShare-94bccb50d11-1561003748&_branch_match_id=670105191114382351&gi=fd8d504494f4)  - 
* [Live Video Transmuxing/Transcoding: FFmpeg vs TwitchTranscoder, Part I](https://blog.twitch.tv/en/2017/10/10/live-video-transmuxing-transcoding-f-fmpeg-vs-twitch-transcoder-part-i-489c1c125f28/)  - 
* [LordCrainer/transcoding_ffmpeg](https://github.com/LordCrainer/transcoding_ffmpeg)  - Transcoding video usando ffmpeg. 
* [Ponyboy47/TranscodeVideo](https://github.com/Ponyboy47/TranscodeVideo)  - A Swift wrapper around the transcode-video command - Ponyboy47/TranscodeVideo
* [SmurfManX/ffmpeg-nvidia-adaptive-vod-transcoder](https://github.com/SmurfManX/ffmpeg-nvidia-adaptive-vod-transcoder)  - bash script which will detect video new file in folder and transcode it to adaprive bitrate - SmurfManX/ffmpeg-nvidia-adaptive-vod-transcoder
* [Snowmix - The Swiss Army Knife of Open Source Live Video Mixing.](https://snowmix.sourceforge.io)  - Snowmix Video Mixer
* [VQEG/streamsim](https://github.com/VQEG/streamsim)  - 
* [Vilsol/Transcoder](https://github.com/Vilsol/Transcoder)  - Docker container to transcode videos in mounted volume to H265 using FFMPEG - Vilsol/Transcoder
* [Zulko/moviepy](https://github.com/Zulko/moviepy)  - 
* [alfg/docker-bento4](https://github.com/alfg/docker-bento4)  - A dockerized Bento4 from source. Built on Alpine Linux.  - alfg/docker-bento4
* [andressspinetti/video-transcoder](https://github.com/andressspinetti/video-transcoder)  - AWS S3 + Lambda + Transcode. 
* [avTranscoder/avTranscoder](https://github.com/avTranscoder/avTranscoder)  - C++ API for LibAV / FFMpeg.d
* [bbc/brave](https://github.com/bbc/brave)  - Basic Real-time AV Editor - allowing you to preview, mix, and route live audio and video streams on the cloud - bbc/brave
* [bbxnet/transcode](https://github.com/bbxnet/transcode)  - 
* [benvanik/node-transcoding](https://github.com/benvanik/node-transcoding)  - node.js video transcoding library. 
* [bfansports/CloudTranscode](https://github.com/bfansports/CloudTranscode)  - Distributed videos and images encoding/transcoding using Amazon SFN, FFMpeg and ImageMagic - bfansports/CloudTranscode
* [bloc97/Anime4K](https://github.com/bloc97/Anime4K)  - A High-Quality Real Time Upscaler for Anime Video.
* [bmhayward/Transcode](https://github.com/bmhayward/Transcode)  - Tools to batch transcode and process videos. 
* [bookyo/express-ffmpeg](https://github.com/bookyo/express-ffmpeg)  - nodejs ffmpeg video transcode webui，基于nodejs的云转码系统 https://www.efvcms.com - bookyo/express-ffmpeg
* [cannonbeach/ott-packager](https://github.com/cannonbeach/ott-packager)  - OTT/ABR streaming encoder (H264/HEVC) and packager for DASH and HLS - cannonbeach/ott-packager
* [chn-lee-yumi/distributed_ffmpeg_transcoding_cluster: 分布式FFMpeg转码集群。A FFMpeg transcoding cluster runs in variable CPUs, including ARM, x86, and others which can run linux. You can use it to run a RaspberryPi cluster.](https://github.com/chn-lee-yumi/distributed_ffmpeg_transcoding_cluster)  - 分布式FFMpeg转码集群。A FFMpeg transcoding cluster runs in variable CPUs, including ARM, x86, and others which can run linux. You can use it to run a RaspberryPi cluster. - chn-lee-yumi/distributed_ffmpeg_...
* [cwinging/transcode](https://github.com/cwinging/transcode)  - python transcode server. 
* [davidbt/djmediastreamer](https://github.com/davidbt/djmediastreamer)  - A Django project that allows you to catalog and stream your videos (using FFmpeg to add subtitles and transcode). - davidbt/djmediastreamer
* [dev-labs-bg/swift-video-generator](https://github.com/dev-labs-bg/swift-video-generator)  - 
* [diego3g/gcloud-node-video-transcoding](https://github.com/diego3g/gcloud-node-video-transcoding)  - 📹🔥 Transcode Google Cloud Storage video files with Node.js and FFmpeg - diego3g/gcloud-node-video-transcoding
* [donmelton/other_video_transcoding](https://github.com/donmelton/other_video_transcoding)  - Other tools to transcode videos. 
* [donmelton/video_transcoding](https://github.com/donmelton/video_transcoding)  - Tools to transcode, inspect and convert videos. 
* [ericgriffin/fflock](https://github.com/ericgriffin/fflock)  - Distributed video transcoding. 
* [escaped/django-video-encoding](https://github.com/escaped/django-video-encoding)  - django-video-encoding helps to convert your videos into different formats and resolutions. - escaped/django-video-encoding
* [fluendo/fluster](https://github.com/fluendo/fluster)  - Testing framework for decoders conformance. 
* [i4tv/gstreamill](https://github.com/i4tv/gstreamill)  - encoder with hls output based on gstreamer. 
* [intel/gmmlib](https://github.com/intel/gmmlib)  - 
* [intel/libva](https://github.com/intel/libva)  - Libva is an implementation for VA-API (Video Acceleration API) - intel/libva
* [intel/media-driver](https://github.com/intel/media-driver)  - 
* [jliljebl/flowblade](https://github.com/jliljebl/flowblade)  - 
* [just-work/django-video-transcoding](https://github.com/just-work/django-video-transcoding)  - Simple video transcoding application for Django Framework - just-work/django-video-transcoding
* [kees/transcode](https://github.com/kees/transcode)  - Video Transcoding Tools. 
* [kwodzicki/video_utils](https://github.com/kwodzicki/video_utils)  - Python package containing many tools useful for converting video files to h264/h265 encoded MP4 or MKV files - kwodzicki/video_utils
* [madebyhiro/codem-transcode](https://github.com/madebyhiro/codem-transcode)  - Offline video transcoder written in node.js. 
* [media-toolbox/avbroadcast: avbroadcast - republish media streams for mass consumption](https://github.com/media-toolbox/avbroadcast)  - avbroadcast - republish media streams for mass consumption - media-toolbox/avbroadcast
* [mltframework/mlt](https://github.com/mltframework/mlt)  - MLT Multimedia Framework.
* [monking/transcode-web-video](https://github.com/monking/transcode-web-video)  - Quickly transcode a source video to MP4, OGV, and WebM, with scale, bitrate, and screengrab options. - monking/transcode-web-video
* [olaris / olaris-server](https://gitlab.com/olaris/olaris-server)  - GitLab.com
* [ptrandev/swift-encoder](https://github.com/ptrandev/swift-encoder)  - A fire-and-forget shell script that encodes multiple video and audio files with ffmpeg. - ptrandev/swift-encoder
* [quarkscript/media_works](https://github.com/quarkscript/media_works)  - Transcode video by ffmpeg with nvenc; normalize the volume; force dynamic range compression to the volume - quarkscript/media_works
* [realeyes-media/demo-encoder](https://github.com/realeyes-media/demo-encoder/)  - A nodejs encoding system based on ffmpeg and configured to write HLS streaming files to S3 - realeyes-media/demo-encoder
* [realeyes-media/demo-encoder](https://github.com/realeyes-media/demo-encoder)  - A nodejs encoding system based on ffmpeg and configured to write HLS streaming files to S3 - realeyes-media/demo-encoder
* [sambios/ffmpeg_transcoder](https://github.com/sambios/ffmpeg_transcoder)  - video transcode based on ffmpeg, support H264/HEVC and more. - sambios/ffmpeg_transcoder
* [selsamman/react-native-transcode](https://github.com/selsamman/react-native-transcode)  - Video Transcoder for React Native. 
* [senko/avtk](https://github.com/senko/avtk)  - 
* [sitkevij/mp](https://github.com/sitkevij/mpi)  - 
* [snickers/snickers](https://github.com/snickers/snickers)  - :chocolate_bar: An open source alternative to the video cloud encoding services. - snickers/snickers
* [streamlink/streamlink](https://github.com/streamlink/streamlink)  - Streamlink is a CLI utility which pipes video streams from various services into a video player - streamlink/streamlink
* [sw360cab/pyup-transcoder](https://github.com/sw360cab/pyup-transcoder)  - a Python-based software to transcode videos and upload files to a remote server or S3-bucket - sw360cab/pyup-transcoder
* [twitter/vireo: Vireo is a lightweight and versatile video processing library written in C++11](https://github.com/twitter/vireo)  - Vireo is a lightweight and versatile video processing library written in C++11 - twitter/vireo
* [voc/voctomix](https://github.com/voc/voctomix)  - Full-HD Software Live-Video-Mixer in python.
* [vt-vl-lab/FGVC](https://github.com/vt-vl-lab/FGVC)  - [ECCV 2020] Flow-edge Guided Video Completion . 
* [xyk2/cloud-transcoder](https://github.com/xyk2/cloud-transcoder)  - Transcoding long (>1 hour) videos quickly and cost-effectively on GCP to adaptive HLS and MP4 mezzanine files. Up to 40x $ savings. - xyk2/cloud-transcoder
* [zolinux/MediaArchiver](https://github.com/zolinux/MediaArchiver)  - Transcode video files using FFMPEG and python3. 

### AV1
*AV1 libraries, tools, examples, and resources.*
[back to top](#readme) 

* [AOMediaCodec/av1-rtp-spec](https://github.com/AOMediaCodec/av1-rtp-spec)  - Current draft (HTML): https://aomediacodec.github.io/av1-rtp-spec/ - AOMediaCodec/av1-rtp-spec
* [AV1 Codec](https://docs.google.com/presentation/d/12_Vewc0SDpB1FycflfT4us9eipRCy0HWJVSaDMDifRs/edit?usp=sharing)  - Working with the AV1 Codec Kevin Staunton-Lambert Solutions Architect R&D @kevleyski www.switch.tv
* [AV1 decoder model](https://norkin.org/research/av1_decoder_model/)  - Description of the AV1 decoder model.
* [Alkl58/NotEnoughAV1Encodes](https://github.com/Alkl58/NotEnoughAV1Encodes)  - GUI Handler for AV1 Encoders (aomenc, rav1e & svt-av1) - Alkl58/NotEnoughAV1Encodes
* [Eyevinn/av1-player](https://github.com/Eyevinn/av1-player)  - Eyevinn AV1 player.
* [Promising Initial Results with AV1 Testing - Streaming Learning Center](https://streaminglearningcenter.com/blogs/promising-initial-results-with-av1-testing.html)  - [vc_row margin_top=”30″][vc_column][vc_column_text]I began testing AV1 early this week. Briefly, my tests involve 16 ten-second clips in four genres (movies, sports, animations, gaming) and an “other” category (music video, nature video). I’ve completed the first set of tests with FFmpeg 4.3, benchmarking x264, x265, and the latest version of the Alliance for Open Media AV1 codec,…
* [SVT-AV1: an open-source AV1 encoder and decoder](https://netflixtechblog.com/svt-av1-an-open-source-av1-encoder-and-decoder-ad295d9b5ca2)  - by Andrey Norkin, Joel Sole, Mariana Afonso, Kyle Swanson, Agata Opalach, Anush Moorthy, Anne Aaron
* [aom - Git at Google](https://aomedia.googlesource.com/aom/)  - 
* [luziferius/av1transcoder](https://github.com/luziferius/av1transcoder)  - Transcode video files to the AV1 format using ffmpeg and libaom-av1. - luziferius/av1transcoder
* [master-of-zen/Av1an: Cross-platform command-line AV1 encode toolkit](https://github.com/master-of-zen/Av1an)  - Cross-platform command-line AV1 encode toolkit. Contribute to master-of-zen/Av1an development by creating an account on GitHub.
* [videolan/dav1d](https://code.videolan.org/videolan/dav1d)  - dav1d is the fastest AV1 decoder on all platforms.
* [xiph/rav1e](https://github.com/xiph/rav1e)  - The fastest and safest AV1 encoder. 

### HEVC
*HEVC (h265) libraries, tools, examples, and resources.*
[back to top](#readme) 

* [515_hls_authoring_update](https://devstreaming-cdn.apple.com/videos/wwdc/2017/515vy4sl7iu70/515/515_hls_authoring_update.pdf)  - 
* [Apple Got It Wrong: Encoding Specs for HEVC in HLS ](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=121878)  - Adding HEVC to your HLS streams is looking like a no brainer, but if you decide to do so, you may not want to take Apple's HEVC encoding recommendations verbatim. You'll deliver noticeably higher quality video if you follow the advice detailed below.
* [Encoding-for-HEVC](https://streaminglearningcenter.com/wp-content/uploads/2018/05/Encoding-for-HEVC-SME-2018-Jan.pdf)  - 
* [Eyevinn/docker-hevc](https://github.com/Eyevinn/docker-hevc)  - Docker container to create HEVC streaming packages - Eyevinn/docker-hevc
* [Guide to HEVC/H.265 Encoding and Playback](https://www.techspot.com/article/1131-hevc-h256-enconding-playback/)  - HEVC's main advantage over H.264 is that it offers roughly double the compression ratio for the same quality. This means that a video file encoded with HEVC can occupy half the space of its H.264 equivalent with no noticeable change in quality, or the same amount of space with improved quality.
* [HEVC in HLS: 10 Key Questions for Streaming Video Developers](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=122637&PageNum=2)  - Many who heard that Apple is adding support for HEVC playback in HTTP Live Streaming were left with more questions than answers. Here's what developers need to know.
* [HEVC/H.265 Video Coding Standard: Part 1](https://www.youtube.com/watch?v=TLNkK5C1KN8&feature=youtu.be)  - Dr. Dan Grois, Benjamin Bross, Dr. Detlev Marpe and Karsten Sühring HEVC/H.265 Video Coding Standart including the Range Extensions Scalable Extensions and M...
* [HEVC/H.265 Video Coding Standard: Part 2](https://www.youtube.com/watch?v=V6a1AW5xyAw&feature=youtu.be)  - Dr. Dan Grois, Benjamin Bross, Dr. Detlev Marpe and Karsten Sühring HEVC/H.265 Video Coding Standart including the Range Extensions Scalable Extensions and M...
* [Standardization of High Efficiency Video Coding (HEVC)](https://youtu.be/p6dLZfs0jTY)  - Standardization of High Efficiency Video Coding (HEVC) Jens-Rainer Ohm, Institute of Communication Engineering, RWTH Aachen University, DE
* [The Market Significance of Apple's Adopting HEVC: Here's What I Think](https://www.linkedin.com/pulse/market-significance-apples-adopting-hevc-heres-what-i-jan-ozer)  - At the recent World Wide Developer's Conference (WWDC), Apple announced that the next versions of Safari, iOS, and tvOS will support HLS with HEVC encoded video. This puts Apple firmly in the HEVC camp, with the Alliance for Open Media camp (Amazon, Cisco, Intel, Google, Microsoft, Mozilla, Netflix,
* [amaurypm/transcode2H265](https://github.com/amaurypm/transcode2H265)  - Unattended video transcoder to H265 and ACC codecs, in MKV containers. - amaurypm/transcode2H265
* [multicoreware / x265 / wiki / Home — Bitbucket](https://bitbucket.org/multicoreware/x265_git/wiki/Home)  - 
* [x265 Documentation — x265  documentation](https://x265.readthedocs.io/en/master/)  - 

### VP9
*VP9 libraries, tools, examples, and resources.*
[back to top](#readme) 


## Transport
*Transport protocols, libraries, and resources.*

* [Wifibroadcast – Analog-like transmission of live video data](https://befinitiv.wordpress.com/wifibroadcast-analog-like-transmission-of-live-video-data/)  - Wifibroadcast is a project aimed at the live transmission of HD video (and other) data using wifi radios. One prominent use case is to transmit camera images for a first person view (FPV) of remote…

### RIST
*Reliable Internet Stream Transport protocol*
[back to top](#readme) 

* [RIST Forum](https://www.rist.tv/)  - The RIST forum manage the Reliable Internet Stream Transport (RIST), for transporting live video over unmanaged networks.
* [librist](https://code.videolan.org/rist/librist)  - A library that can be used to easily add the RIST protocol to your application.

### RTMP
*Real-Time Messaging Protocol*
[back to top](#readme) 

* [Create your own video streaming server with Linux](https://opensource.com/article/19/1/basic-live-video-streaming-server)  - Using Nginx to create a streaming server using RTMP and nginx
* [The Real-Time Messaging Protocol Explained](https://www.wowza.com/blog/rtmp-streaming-real-time-messaging-protocol)  - 

### SRT
*Secure Reliable Transport protocol*
[back to top](#readme) 

* [SRT Alliance](https://www.srtalliance.org/)  - Home page for the SRT protocol
* [SRT Cookbook](https://srtlab.github.io/srt-cookbook/)  - More in-depth technical documentaion on the SRT protocol and library.
* [SRT Open Source project](https://github.com/Haivision/srt)  - 
* [Streaming With SRT Protocol in OBS](https://obsproject.com/wiki/Streaming-With-SRT-Protocol)  - 

## Streaming Server and Storage
*Packagers, origins (s3, gcs), and data movement for linear and finite playback. *

* [OpenVisualCloud/Smart-City-Sample](https://github.com/OpenVisualCloud/Smart-City-Sample)  - The smart city reference pipeline shows how to integrate various media building blocks, with analytics powered by the OpenVINO™ Toolkit, for traffic or stadium sensing, analytics and management tas...
* [Red5/red5-server](https://github.com/Red5/red5-server)  - Red5 Server core. 
* [Roverr/rtsp-stream](https://github.com/Roverr/rtsp-stream)  - Out of box solution for RTSP - HLS live stream transcoding. Makes RTSP easy to play in browsers. - Roverr/rtsp-stream
* [ant-media/Ant-Media-Server](https://github.com/ant-media/Ant-Media-Server)  - Ant Media Server supports RTMP, RTSP, WebRTC and Adaptive Bitrate. It can also record videos in MP4, HLS and FLV - ant-media/Ant-Media-Server
* [haiwen/seafile](https://github.com/haiwen/seafile)  - High performance file syncing and sharing, with also Markdown WYSIWYG editing, Wiki, file label and other knowledge management features. - haiwen/seafile
* [ireader/media-server](https://github.com/ireader/media-server)  - RTSP/RTP/RTMP/FLV/HLS/MPEG-TS/MPEG-PS/MPEG-DASH/MP4/fMP4 - ireader/media-server
* [muxinc/stream.new](https://github.com/muxinc/stream.new)  - The repo for https://stream.new. 
* [openfun/marsha](https://github.com/openfun/marsha)  - :clapper: A self-hosted opensource LTI video provider - openfun/marsha
* [openstack/swift](https://github.com/openstack/swift)  - OpenStack Storage (Swift).
* [ossrs/srs](https://github.com/ossrs/srs)  - SRS is a simple live streaming cluster, a simple joy. - ossrs/srs
* [prologic/tube](https://github.com/prologic/tube)  - 📺 a Youtube-like (without censorship and features you don&#39;t need!) Video Sharing App written in Go which also supports automatic transcoding to MP4 H.265 AAC, multiple collections and R...
* [rclone/rclone](https://github.com/rclone/rclone)  - rsync for cloud storage - Google Drive, Amazon Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Cloudfiles, Google Cloud Storage, Yandex Files - rclone/rclone
* [streamaserver/streama](https://github.com/streamaserver/streama)  - Self hosted streaming media server. https://docs.streama-project.com/ - streamaserver/streama

## Specs and Standards
*Latest offical specs and standards related to video streaming.*

* [DASH-IF IOPs](https://dashif.org/guidelines/)  - 
* [How Do I Become an ANSI Member](https://www.ansi.org/membership/how_to_join/how_3)  - 
* [latest HLS Spec](https://tools.ietf.org/html/draft-pantos-hls-rfc8216bis-08)  - 

### Industry Forums
*Industry forums relative to video streaming.*
[back to top](#readme) 

* [CTA | WAVE Project](https://cta.tech/Resources/Standards/WAVE-Project)  - The WAVE (Web Application Video Ecosystem) Project, hosted by the Consumer Technology Association (CTA)®, aims to improve how internet-delivered commercial video is handled on consumer electronics devices and to make it easier for content creators to distribute video to those devices.
* [Home | Streaming Video Alliance](https://www.streamingvideoalliance.org/)  - Making Streaming Video Better Streaming video is exploding in popularity. Consumers are watching more video online across a myriad of devices. But, the streaming experiences, across providers, can be wildly different from each other which ultimately hurts adoption. The problem is a lack of colla ...

### MPEG
*MPEG meetings, standards, and resources. *
[back to top](#readme) 

* [ISO Base Media File Format Reference Software](https://github.com/MPEGGroup/isobmff)  - 
* [MPEG About](https://www.mpegstandards.org/about-mpeg/)  - 
* [MPEG High Efficiency Image File Format (HEIF)](https://nokiatech.github.io/heif/)  - 
* [MPEG Meetings](https://www.mpegstandards.org/meetings/)  - 
* [MPEG future](http://mpegfuture.org/)  - 
* [MPEG home page](https://www.mpegstandards.org)  - 
* [MPEG point cloud compression](https://mpeg-pcc.org)  - 
* [MPEG: What Happened?](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=141678)  - At the end of last month, MPEG co-founder Leonardo Chiariglione announced the 'MPEG is closed.' That's not quite true, but it is undergoing a reorganization. So what does that mean for the organization and the new codec standards it is bringing out this year?
* [Official Registration Authority for the ISOBMFF family of standards](http://mp4ra.org/)  - 

## Players
*Client players, libraries, tools, and examples.*

* [Building native video Pins](https://medium.com/pinterest-engineering/building-native-video-pins-7ff89ad3ec33)  - Billions of videos are viewed across the internet every day, but video on Pinterest is unique. On Pinterest, you’ve always been able to save videos from around the web, and in 2013, we made it…
* [IvanoBilenchi/Adaptive-Video-Player](https://github.com/IvanoBilenchi/Adaptive-Video-Player)  - HLS player for iOS that supports manual selection for the quality of adaptive streams - IvanoBilenchi/Adaptive-Video-Player
* [Samples players for dash.js](http://reference.dashif.org/dash.js/latest/samples/index.html)  - 
* [adrg/libvlc-go](https://github.com/adrg/libvlc-go)  - Go bindings for libVLC and high-level media player interface.
* [elements/packages/mux-player](https://github.com/muxinc/elements/tree/main/packages/mux-player)  - `<mux-player>` is the official Mux-flavored video player web component. The player UI is built on [Media Chrome](https://github.com/muxinc/media-chrome) and [`<mux-video>`](https://github.com/muxinc/elements/tree/main/packages/mux-video) drives the core video logic used to play Mux Video content.
* [imoreapps/ffmpeg-avplayer-for-ios-tvos](https://github.com/imoreapps/ffmpeg-avplayer-for-ios-tvos)  - A tiny but powerful iOS and Apple TV OS av player framework that's based on the FFmpeg library. - imoreapps/ffmpeg-avplayer-for-ios-tvos
* [lightspark/lightspark](https://github.com/lightspark/lightspark)  - An open source flash player implementation.
* [matvp91/indigo-player](https://github.com/matvp91/indigo-player)  - Highly extensible, modern, JavaScript video player. Handles MPEG-Dash / HLS / MPEG-4 and is built on top of the HTML5 video element. - matvp91/indigo-player
* [mpv-player/mpv](https://github.com/mpv-player/mpv)  - 🎥 Command line video player.
* [nytimes/ios-360-videos](https://github.com/nytimes/ios-360-videos)  - NYT360Video plays 360-degree video streamed from an AVPlayer on iOS. - nytimes/ios-360-videos
* [peak3d/inputstream.adaptive](https://github.com/peak3d/inputstream.adaptive)  - kodi inputstream addon for several manifest types.
* [ruffle-rs/ruffle](https://github.com/ruffle-rs/ruffle)  - A Flash Player emulator written in Rust.
* [tjenkinson/media-element-syncer](https://github.com/tjenkinson/media-element-syncer)  - Synchronise two or more HTML5 media elements.
* [ustwo/videoplayback-ios](https://github.com/ustwo/videoplayback-ios)  - Swift AVPlayer wrapper using the VIPER architecture. Currently a work in progress  - ustwo/videoplayback-ios
* [videolan/libvlcsharp](https://github.com/videolan/LibVLCSharp)  - Cross-platform .NET/Mono bindings for LibVLC
* [videolan/vlc](https://github.com/videolan/vlc)  - VLC media player - All pull requests are ignored, please follow https://wiki.videolan.org/Sending_Patches_VLC/ - videolan/vlc
* [vitalets/awesome-smart-tv](https://github.com/vitalets/awesome-smart-tv)  - :zap:A curated list of awesome resources for building Smart TV apps - vitalets/awesome-smart-tv

### Android
*Android and fireTV tools, sdks, and examples.*
[back to top](#readme) 

* [google/ExoPlayer](https://github.com/google/ExoPlayer)  - ExoPlayer is an application level media player for Android.
* [mkaflowski/HybridMediaPlayer](https://github.com/mkaflowski/HybridMediaPlayer)  - Android music and video player. Uses ExoPlayer 2 and MediaPlayer for lower APIs and makes using ExoMediaPlayer easier. If you need advanced options such as handling Chromecast it is delivered by Ex...
* [videolan/vlc-android](https://code.videolan.org/videolan/vlc-android)  - VLC for Android, Android TV and ChromeOS.

### Chromecast
*Chromecast app tools, libraries,and examples.*
[back to top](#readme) 

* [Build a basic Cast Receiver](https://codelabs.developers.google.com/codelabs/cast-receiver/#0)  - 
* [googlecast/CastReceiver](https://github.com/googlecast/CastReceiver)  - Reference Receiver: CastReceiver shows how to develop a fully Cast Design Checklist compliant receiver with additional features. - googlecast/CastReceiver

### iOS tvOS
*AVPlayer, playback tools, sdks, and examples.*
[back to top](#readme) 

* [BrikerMan/BMPlayer](https://github.com/BrikerMan/BMPlayer)  - A video player for iOS, based on AVPlayer, support the horizontal, vertical screen. support adjust volume, brightness and seek by slide, support subtitles.  - BrikerMan/BMPlayer
* [DaMingShen/SUCacheLoader](https://github.com/DaMingShen/SUCacheLoader)  - AVPlayer 
* [DeviLeo/DLGPlayer](https://github.com/DeviLeo/DLGPlayer)  - A media player for iOS based on FFmpeg 4.0.
* [MPEGDASHPlayer/MPEGDASH-iOS-Player](https://github.com/MPEGDASHPlayer/MPEGDASH-iOS-Player)  - The MPEG-DASH Player iOS Application.
* [SRGSSR/srgmediaplayer-apple](https://github.com/SRGSSR/srgmediaplayer-apple)  - An advanced media player library, simple and reliable - SRGSSR/srgmediaplayer-apple
* [StyleShare/HLSCachingReverseProxyServer](https://github.com/StyleShare/HLSCachingReverseProxyServer)  - A simple local reverse proxy server for HLS segment cache - StyleShare/HLSCachingReverseProxyServer
* [VeinGuo/VGPlayer](https://github.com/VeinGuo/VGPlayer)  - 📺  A simple iOS video player by Vein.
* [google/shaka-player-embedded](https://github.com/google/shaka-player-embedded)  - Shaka Player in a C++ Framework. 
* [googleads/google-media-framework-ios](https://github.com/googleads/google-media-framework-ios)  - The Google Media Framework (GMF) is a lightweight media player designed to make video playback and integration with the Google IMA SDK on iOS easier. - googleads/google-media-framework-ios
* [hanton/HTY360Player](https://github.com/hanton/HTY360Player)  - Open Source iOS 360 Degree Panorama Video Player.
* [iina/iina](https://github.com/iina/iina)  - The modern video player for macOS.
* [kodlian/TVVLCPlayer](https://github.com/kodlian/TVVLCPlayer)  - TVVLCPlayer lets you integrate easily a powerfull video player with playback control views to your tvOS apps. - kodlian/TVVLCPlayer
* [libobjc/SGPlayer](https://github.com/libobjc/SGPlayer)  - A powerful media play framework for iOS, macOS, and tvOS. - libobjc/SGPlayer
* [noreasonprojects/ModernAVPlayer](https://github.com/noreasonprojects/ModernAVPlayer)  - ModernAVPlayer is a persistence AVPlayer wrapper. 
* [piemonte/Player](https://github.com/piemonte/Player)  - ▶️ video player in Swift, simple way to play and stream media on iOS/tvOS - piemonte/Player
* [renzifeng/ZFPlayer](https://github.com/renzifeng/ZFPlayer)  - Support customization of any player SDK and control layer
* [rinsuki/HWAcceleratedVP9Player](https://github.com/rinsuki/HWAcceleratedVP9Player)  - Hardware Accelerated VP9 Player in macOS 11.0 Big Sur beta 4+ - rinsuki/HWAcceleratedVP9Player
* [tanersener/mobile-ffmpeg](https://github.com/tanersener/mobile-ffmpeg)  - FFmpeg for Android, iOS and tvOS.
* [videolan/vlc-ios](https://code.videolan.org/videolan/vlc-ios)  - VLC for iOS is the official port of VLC on the iOS/tvOS platforms.
* [vitoziv/VIMediaCache](https://github.com/vitoziv/VIMediaCache)  - Cache media file while play media using AVPlayer.
* [wxxsw/GSPlayer](https://github.com/wxxsw/GSPlayer)  - ⏯ Video player, support for caching, preload, fullscreen transition and custom control view. 视频播放器，支持边下边播、预加载、全屏转场和自定义控制层 - wxxsw/GSPlayer
* [xiewei-wayne/FFEngine.framework](https://github.com/xiewei-wayne/FFEngine.framework)  - FFEngine framework is a high performance player sdk for iOS based on ffmpeg. - xiewei-wayne/FFEngine.framework
* [xiewei-wayne/rtmp-video-player-for-ios](https://github.com/xiewei-wayne/rtmp-video-player-for-ios)  - Based on FFEngine framework, a rtmp video player for apple iOS devices. - xiewei-wayne/rtmp-video-player-for-ios

### Roku
*Roku app tools, libraries,and examples.*
[back to top](#readme) 

* [CCecilia/roku-suite-desktop](https://github.com/CCecilia/roku-suite-desktop)  - Tool suite for Roku channel development.
* [MediaBrowser/Emby.Roku](https://github.com/MediaBrowser/Emby.Roku)  - Emby for Roku. 
* [T-Pham/RokuJSONHelperNode](https://github.com/T-Pham/RokuJSONHelperNode)  - Roku SceneGraph JSON Helper.
* [XML + Code + Good times = RSG Application](https://medium.com/plexlabs/xml-code-good-times-rsg-application-b963f0cec01b)  - Written by John Zolezzi — April 6th 2018
* [anachirino/bifserver](https://github.com/anachirino/bifserver)  - Server which creates and serves up BIF files for Roku players - anachirino/bifserver
* [briandunnington/Redoku](https://github.com/briandunnington/Redoku)  - Redux for Roku.
* [briandunnington/Roact](https://github.com/briandunnington/Roact)  - React for Roku
* [chrishoffman/brightscript-json](https://github.com/chrishoffman/brightscript-json)  - JSON parser for Roku's proprietary Brightscript language - chrishoffman/brightscript-json
* [dphang/roku-lib](https://github.com/dphang/roku-lib)  - Some useful Roku utilities.
* [exegersha/network-benchmark](https://github.com/exegersha/network-benchmark)  - Proof of concept. Roku app implementing network layer using scene graph nodes. - exegersha/network-benchmark
* [gabek/Amplitude-Brightscript](https://github.com/gabek/Amplitude-Brightscript)  - A Brightscript (Roku) library for submitting analytics to Amplitude - gabek/Amplitude-Brightscript
* [gabek/SegmentIO-Brightscript](https://github.com/gabek/SegmentIO-Brightscript)  - A BrightScript interface to SegmentIO event tracking - gabek/SegmentIO-Brightscript
* [georgejecook/rooibos](https://github.com/georgejecook/rooibos)  - simple, flexible, fun brightscript test framework for roku scenegraph apps - georgejecook/rooibos
* [juliomalves/roku-libs](https://github.com/juliomalves/roku-libs)  - BrightScript Utility Libraries.
* [karimkawambwa/roku-framework](https://github.com/karimkawambwa/roku-framework)  - Roku app framework to make app creation easier and structured. Under construction - karimkawambwa/roku-framework
* [karimkawambwa/roku-framework-example](https://github.com/karimkawambwa/roku-framework-example)  - This is a project to show how the boku-framework by Karim Kawambwa is used - karimkawambwa/roku-framework-example
* [mrkjffrsn/RokuFramework](https://github.com/mrkjffrsn/RokuFramework)  - An opensource Roku framework.
* [nod/rokumote](https://github.com/nod/rokumote)  - osx app for controlling your roku because sometimes your kids lose the remote - nod/rokumote
* [rkoshak/sensorReporter](https://github.com/rkoshak/sensorReporter)  - A python based service that receives sensor inputs and publishes them over REST (should work with any API but mainly tested with openHAB) or MQTT. It can also receive commands and perform an action...
* [rokucommunity/brighterscript-formatter](https://github.com/RokuCommunity/brighterscript-formatter)  - A code formatter for BrighterScript (and BrightScript) - rokucommunity/brighterscript-formatter
* [rokucommunity/vscode-brightscript-language](https://github.com/rokucommunity/vscode-brightscript-language)  - A Visual Studio Code extension for Roku's BrightScript language - rokucommunity/vscode-brightscript-language
* [rokudev/RAF4RSG-sample](https://github.com/rokudev/RAF4RSG-sample)  - sample demonstrating the Roku Advertising Framework in SceneGraph - rokudev/RAF4RSG-sample
* [rokudev/SDK-Development-Guide](https://github.com/rokudev/SDK-Development-Guide)  - Contribute to rokudev/SDK-Development-Guide development by creating an account on GitHub.
* [rokudev/SceneGraphDeveloperExtensions](https://github.com/rokudev/SceneGraphDeveloperExtensions)  - Contribute to rokudev/SceneGraphDeveloperExtensions development by creating an account on GitHub.
* [rokudev/automated-channel-testing](https://github.com/rokudev/automated-channel-testing)  - Roku Automated Channel Testing: Selenium-based WebDriver + Robot Framework + Samples - rokudev/automated-channel-testing
* [rokudev/dolby-audio-sample](https://github.com/rokudev/dolby-audio-sample)  - A collection of Dolby test content available in different streaming protocols. - rokudev/dolby-audio-sample
* [rokudev/samples](https://github.com/rokudev/samples)  - Collection of sample channels for side-loading on your Roku device - rokudev/samples
* [rokudev/unit-testing-framework](https://github.com/rokudev/unit-testing-framework)  - Tool for automating and testing Roku channels.
* [rokudev/videoplayer-channel](https://github.com/rokudev/videoplayer-channel)  - SceneGraph version of the SDK1 VideoPlayer Channel  - rokudev/videoplayer-channel
* [rolandoislas/BrightWebSocket](https://github.com/rolandoislas/BrightWebSocket)  - RFC 6455 WebSocket Library for the Roku.
* [schtanislau/brightscript-state-machine](https://github.com/schtanislau/brightscript-state-machine)  - State management for Roku channel..
* [sjbarag/brs-testbed](https://github.com/sjbarag/brs-testbed)  - A simple, buildable Roku channel that executes arbitrary BrightScript files. - sjbarag/brs-testbed
* [veeta-tv/jasmine-roku](https://github.com/veeta-tv/jasmine-roku)  - Example jasmine tests using node-roku-test for verifying Roku channel behavior - veeta-tv/jasmine-roku
* [willowtreeapps/ukor](https://github.com/willowtreeapps/ukor)  - A Roku build tool with support for build flavors.
* [zype/zype-roku-scenegraph](https://github.com/zype/zype-roku-scenegraph)  - Contribute to zype/zype-roku-scenegraph development by creating an account on GitHub.

### Smart TVs
[back to top](#readme) 


### Web
*Web browser player, tools, sdks, and examples.*
[back to top](#readme) 

* [Chimeejs/chimee](https://github.com/Chimeejs/chimee)  - a video player framework aims to bring wonderful experience on browser - Chimeejs/chimee
* [Dash JavaScript Player](http://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html)  - 
* [Eyevinn/abr-player-chrome](https://github.com/Eyevinn/abr-player-chrome)  - Chrome extension that uses Eyevinn HTML player to be able to play HLS and MPEG-DASH natively - Eyevinn/abr-player-chrome
* [Eyevinn/channel-engine-multiview](https://github.com/Eyevinn/channel-engine-multiview)  - A multiview frontend for Eyevinn Channel Engine.
* [Eyevinn/docker-html5player](https://github.com/Eyevinn/docker-html5player)  - A Docker containerized HTML5 player based on Shaka Player - Eyevinn/docker-html5player
* [Eyevinn/eyevinn-player](https://github.com/Eyevinn/eyevinn-player)  - Throttled video player to test video streams.
* [Eyevinn/ott-multiview](https://github.com/Eyevinn/ott-multiview)  - This is a web based multiview screen for HLS and MPEG-DASH streams based on hls.js and Shaka Player. - Eyevinn/ott-multiview
* [GeneticGenesis/phils-players](https://github.com/GeneticGenesis/phils-players)  - A collection of video players with vaguely simple GUIs for video engineers. - GeneticGenesis/phils-players
* [MoePlayer/DPlayer](https://github.com/MoePlayer/DPlayer)  - :lollipop: Wow, such a lovely HTML5 danmaku video player - MoePlayer/DPlayer
* [bbc/bigscreen-player](https://github.com/bbc/bigscreen-player)  - Simplified media playback for bigscreen devices.
* [bytedance/xgplayer](https://github.com/bytedance/xgplayer)  - A HTML5 video player with a parser that saves traffic - bytedance/xgplayer
* [epiclabs-io/epic-video-comparator](https://github.com/epiclabs-io/epic-video-comparator)  - Javascript library which implements a video comparator component: two overlaped and synchronized video players each one playing an independent source. - epiclabs-io/epic-video-comparator
* [foxford/react-hls](https://github.com/foxford/react-hls)  - React component for HLS player. 
* [mediaelement/mediaelement](https://github.com/mediaelement/mediaelement)  - HTML5 &lt;audio&gt; or &lt;video&gt; player with support for MP4, WebM, and MP3 as well as HLS, Dash, YouTube, Facebook, SoundCloud and others with a common HTML5 MediaElement API, ...
* [sampotts/plyr](https://github.com/sampotts/plyr)  - A simple HTML5, YouTube and Vimeo player.
* [video-dev/hls.js](https://github.com/video-dev/hls.js)  - JavaScript HLS client using Media Source Extension - video-dev/hls.js
* [videogular/videogular](https://github.com/videogular/videogular)  - The HTML5 video player for AngularJS. 
* [videojs/http-streaming](https://github.com/videojs/http-streaming)  - HLS, DASH, and future HTTP streaming protocols library for video.js - videojs/http-streaming
* [videojs/video.js](https://github.com/videojs/video.js)  - Video.js - open source HTML5 & Flash video player.
* [vimond/replay](https://github.com/vimond/replay)  - A React video player facilitating adaptive stream playback with custom UI and a React-friendly API. - vimond/replay

## FFMPEG
*FFMPEG libraries, configs, tools, and examples.*

* [2501world/transcoding-performance-trial: Runs FFmpeg transcoding processes simultaneously and measures CPU performance](https://github.com/2501world/transcoding-performance-trial)  - Runs FFmpeg transcoding processes simultaneously and measures CPU performance - 2501world/transcoding-performance-trial
* [AlvianPrasetya/transcoding: FFmpeg transcoders benchmark](https://github.com/AlvianPrasetya/transcoding)  - FFmpeg transcoders benchmark. Contribute to AlvianPrasetya/transcoding development by creating an account on GitHub.
* [Azure-Samples/batch-python-ffmpeg-tutorial](https://github.com/Azure-Samples/batch-python-ffmpeg-tutorial)  - A Python application that uses Batch to process media files in parallel with the ffmpeg open-source tool. - Azure-Samples/batch-python-ffmpeg-tutorial
* [CUDA GPU Accelerated h264/h265/HEVC Video Encoding with ffmpeg](https://ntown.at/de/knowledgebase/cuda-gpu-accelerated-h264-h265-hevc-video-encoding-with-ffmpeg/)  - How to use CUDA GPU hardware encoding with ffmpeg to encode h264 and h264 HEVC movies in high quality and highspeed with our optimized parameter settings.
* [Ch00k/ffmpy](https://github.com/Ch00k/ffmpy)  - 
* [ColorlabMD/FFCommand_Engine](https://github.com/ColorlabMD/FFCommand_Engine)  - Create and execute FFmpeg commands. 
* [Correcting for audio/video sync issues with the ffmpeg program’s ITSOFFSET switch](https://wjwoodrow.wordpress.com/2013/02/04/correcting-for-audiovideo-sync-issues-with-the-ffmpeg-programs-itsoffset-switch/)  - The ffmpeg program has numerous “switches” that help to adjust and convert audio and video files. Some of them are not explained very well in the documentation, and many websites have c…
* [ElderByte-/docker-java-media](https://github.com/ElderByte-/docker-java-media)  - JRE 10 (Java 10) and media tools (ffmpeg).
* [FFmpeg/FFV1](https://github.com/FFmpeg/FFV1)  - The FFV1 lossless video codec specification. 
* [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)  - Mirror of git://source.ffmpeg.org/ffmpeg.git.
* [FallingSnow/h265ize](https://github.com/FallingSnow/h265ize)  - A node utility utilizing ffmpeg to encode videos with the hevc codec. - FallingSnow/h265ize
* [Generate MPEG-TS from file with ffmpeg](https://medium.com/@eyevinntechnology/generate-mpeg-ts-from-file-with-ffmpeg-7561181e6369?source=userActivityShare-94bccb50d11-1560983471&_branch_match_id=670020142756633081)  - In this post I will describe how an MPEG-TS multicast stream can be generated with ffmpeg by looping an MP4 file and a Docker container…
* [How to decode a video (memory file / byte string) and step through it frame by frame in python?](https://stackoverflow.com/questions/60558412/how-to-decode-a-video-memory-file-byte-string-and-step-through-it-frame-by-f)  - I am using python to do some basic image processing, and want to extend it to process a video frame by frame. I get the video as a blob from a server - .webm encoded - and have it in python as a b...
* [How to generate a fmp4 hls live stream with FFMPEG](https://nomadyun.wordpress.com/2018/04/12/how-to-generate-a-fmp4-hls-live-stream-with-ffmpeg/)  - ffmpeg -re -stream_loop -1 -i voweb.mp4 -hls_fmp4_init_filename init.mp4 -vf “settb=AVTB,setpts=’trunc(PTS/1K)*1K+st\(1,trunc(RTCTIME/1K))-1K*trunc(ld(1)/1K)’,\ drawtext=fontfile=…
* [Is it possible to get FFmpeg to use hardware acceleration for HEVC transcoding on macOS?](https://superuser.com/questions/1295957/ffmpeg-and-hardware-acceleration-of-hevc-transcoding-on-mac)  - I have a MacBook Pro with a Kaby Lake processor running macOS High Sierra (10.12). Is it possibe somehow to setup FFmpeg to utilize hardware encoding of HEVC with toolbox, instead of libx265?
* [Kagami/ffmpeg.js](https://github.com/Kagami/ffmpeg.js)  - Port of FFmpeg with Emscripten.
* [Loop file and generate multiple video bitrates muxed in MPEG-TS with ffmpeg](https://medium.com/@eyevinntechnology/loop-file-and-generate-multiple-video-bitrates-muxed-in-mpeg-ts-with-ffmpeg-85658d0b74bb?source=userActivityShare-94bccb50d11-1560983383&_branch_match_id=670019768959110835)  - In a previous post I described how an MPEG-TS multicast stream can be generated with ffmpeg by looping an MP4 file. In this post I will…
* [Mozilla-Open-Lab-Etwas/Video-Transcoder](https://github.com/Mozilla-Open-Lab-Etwas/Video-Transcoder)  - FFMPEG Wasm Video Transcoder. 
* [NVIDIA/nvidia-docker](https://github.com/NVIDIA/nvidia-docker)  - Build and run Docker containers leveraging NVIDIA GPUs - NVIDIA/nvidia-docker
* [Saurabh702/ffmpeg-scale-benchmark](https://github.com/Saurabh702/ffmpeg-scale-benchmark)  - 
* [This gist will generate an Intel QSV-enabled FFmpeg build using the open source Intel Media SDK. Testbed used: Ubuntu 18.04LTS. A fallback is also provided for the intel vaapi driver where needed.](https://gist.github.com/SeanMollet/0eed16e80630ab67532890a9d42132af)  - This gist will generate an Intel QSV-enabled FFmpeg build using the open source Intel Media SDK. Testbed used: Ubuntu 18.04LTS. A fallback is also provided for the intel vaapi driver where needed. ...
* [Understanding Rate Control Modes (x264, x265, vpx)](https://slhck.info/video/2017/03/01/rate-control.html)  - What is “rate control”? It’s what a video encoder does when it decides how many bits to spend for a given frame. The goal of (lossy) video encoding is to sav...
* [VCDP/FFmpeg-patch](https://github.com/VCDP/FFmpeg-patch)  - This repository contains a collection of FFmpeg* patches and samples to enable CNN model based video analytics capabilities (such as object detection, classification, recognition) in FFmpeg* framew...
* [WritingMinds/ffmpeg-android-java](https://github.com/WritingMinds/ffmpeg-android-java)  - Android java library for FFmpeg binary compiled using https://github.com/writingminds/ffmpeg-android - WritingMinds/ffmpeg-android-java
* [albanie/shot-detection-benchmarks: A comparison of ffmpeg, Shotdetect and PySceneDetect for shot transition detection](https://github.com/albanie/shot-detection-benchmarks)  - A comparison of ffmpeg, Shotdetect and PySceneDetect for shot transition detection - albanie/shot-detection-benchmarks
* [bcoudurier/FFmbc](https://github.com/bcoudurier/FFmbc)  - FFmpeg customized for broadcast and professional usage - bcoudurier/FFmbc
* [binoculars/aws-lambda-ffmpeg](https://github.com/binoculars/aws-lambda-ffmpeg)  - An S3-triggered Amazon Web Services Lambda function that runs your choice of FFmpeg 🎬 commands on a file  🎥 and uploads the outputs to a bucket. - binoculars/aws-lambda-ffmpeg
* [bramp/ffmpeg-cli-wrapper](https://github.com/bramp/ffmpeg-cli-wrapper)  - Java wrapper around the FFmpeg command line tool.
* [cash2one/VideoTranscoding-Backend](https://github.com/cash2one/VideoTranscoding-Backend)  - This application transcode a video that you send on all formats what you want and diferent resolutions. - cash2one/VideoTranscoding-Backend
* [compile and install latest ffmpeg source as pkg](https://gist.github.com/krzemienski/e51a0b7a6ba77e616f954e516783270c#file-compile-and-install-latest-ffmpeg-source-sh-L2)  - compile and install latest ffmpeg source as pkg. GitHub Gist: instantly share code, notes, and snippets.
* [cuda/ubuntu16.04/ffmpeg-gpu/Dockerfile · master · nvidia / container-images / samples](https://gitlab.com/nvidia/container-images/samples/blob/master/cuda/ubuntu16.04/ffmpeg-gpu/Dockerfile)  - Sample Dockerfiles for Docker Hub images
* [ffmprovisr](https://amiaopensource.github.io/ffmprovisr)  - Cookbook of commonly used FFmpeg recipes with descriptions of how each command works and how to modify it to fit your needs
* [fluent-ffmpeg/node-fluent-ffmpeg](https://github.com/fluent-ffmpeg/node-fluent-ffmpeg)  - A fluent API to FFMPEG (http://www.ffmpeg.org). 
* [git-developer/vaapi-video-converter](https://github.com/git-developer/vaapi-video-converter)  - A docker-based video converter that uses VAAPI-compatible hardware for transcoding - git-developer/vaapi-video-converter
* [gitfu/manifesto](https://github.com/gitfu/manifesto)  - Manifesto is an HLS tool for creating multiple variants, a master.m3u8 file, and converting 608 captions to segmented webvtt subtitles via ffmpeg. - gitfu/manifesto
* [imageio/imageio-ffmpeg](https://github.com/imageio/imageio-ffmpeg)  - FFMPEG wrapper for Python. 
* [intel/intel-vaapi-driver](https://github.com/intel/intel-vaapi-driver)  - VA-API user mode driver for Intel GEN Graphics family - intel/intel-vaapi-driver
* [intel/vaapi-fits](https://github.com/intel/vaapi-fits)  - 
* [jonghwanhyeon/python-ffmpeg](https://github.com/jonghwanhyeon/python-ffmpeg)  - A python interface for FFmpeg using asyncio. 
* [jrottenberg/ffmpeg](https://github.com/jrottenberg/ffmpeg)  - Docker build for FFmpeg on Ubuntu / Alpine / Centos 7 / Scratch - jrottenberg/ffmpeg
* [kewlbear/FFmpeg-iOS-build-script](https://github.com/kewlbear/FFmpeg-iOS-build-script)  - Shell scripts to build FFmpeg for iOS and tvOS. 
* [kkroening/ffmpeg-python](https://github.com/kkroening/ffmpeg-python)  - 
* [kokorin/Jaffree](https://github.com/kokorin/Jaffree)  - Java ffmpeg and ffprobe command-line wrapper.
* [linuxserver/docker-ffmpeg](https://github.com/linuxserver/docker-ffmpeg)  - 
* [markus-perl/ffmpeg-build-script](https://github.com/markus-perl/ffmpeg-build-script)  - The FFmpeg build script provides an easy way to build a static FFmpeg on OSX and Linux with non-free codecs included. - markus-perl/ffmpeg-build-script
* [microshow/RxFFmpeg](https://github.com/microshow/RxFFmpeg)  - 🔥RxFFmpeg 是基于 ( FFmpeg 4.0 + X264 + mp3lame + fdk-aac )
* [mitio/useful-ffmpeg-commands: A collection of FFmpeg commands taken from practice](https://github.com/mitio/useful-ffmpeg-commands)  - A collection of FFmpeg commands taken from practice - mitio/useful-ffmpeg-commands
* [mugiseyebrows/mugi-ffmpeg](https://github.com/mugiseyebrows/mugi-ffmpeg)  - Gui for ffmpeg to simplify transcoding and embeding audio / subtitles in mkv videos - mugiseyebrows/mugi-ffmpeg
* [nextbreakpoint/ffmpeg4java](https://github.com/nextbreakpoint/ffmpeg4java)  - FFmpeg4Java provides a JNI wrapper of FFmpeg library - nextbreakpoint/ffmpeg4java
* [okorach/audio-video-tools](https://github.com/okorach/audio-video-tools)  - Python based batch tools to transcode audio and video conveniently (leverages FFMpeg) - okorach/audio-video-tools
* [phaux/node-ffmpeg-stream](https://github.com/phaux/node-ffmpeg-stream)  - Node.js bindings to ffmpeg command, exposing stream based API - phaux/node-ffmpeg-stream
* [pyke369/sffmpeg](https://github.com/pyke369/sffmpeg)  - Full-featured static FFmpeg build helper. 
* [rdp/ffmpeg-windows-build-helpers](https://github.com/rdp/ffmpeg-windows-build-helpers)  - Helper script for cross compiling some media tools for windows, like customizable ffmpeg.exe (with or without non-free components, etc), and some other bonuses like mplayer, mp4box, mxf, etc. - rdp...
* [scivision/PyLivestream](https://github.com/scivision/PyLivestream)  - Pure Python FFmpeg-based live video / audio streaming to YouTube, Facebook, Periscope, Twitch, and more - scivision/PyLivestream
* [serverlesspub/ffmpeg-aws-lambda-layer](https://github.com/serverlesspub/ffmpeg-aws-lambda-layer)  - FFmpeg/FFprobe AWS Lambda layer. 
* [silencecorner/jre-ffmpeg-apline](https://github.com/silencecorner/jre-ffmpeg-apline)  - Dockerfile [jre8](https://github.com/fabric8io-images/java) and [ffmpeg](https://hub.docker.com/r/jrottenberg/ffmpeg)  - silencecorner/jre-ffmpeg-apline
* [slhck/ffmpeg-encoding-course](https://github.com/slhck/ffmpeg-encoding-course)  - An introduction to FFmpeg and its tools. 
* [slhck/rate-control-tests: Tests for different rate control modes in x264](https://github.com/slhck/rate-control-tests)  - Tests for different rate control modes in x264. Contribute to slhck/rate-control-tests development by creating an account on GitHub.
* [sunhailin-Leo/AutoConfigShellScript: Automatically compile and configure ffmpeg, Python 3.7.2(default), PyAV, OpenCV, Keras, Tensorflow(CPU Mode) and other relative environment.](https://github.com/sunhailin-Leo/AutoConfigShellScript)  - Automatically compile and configure ffmpeg, Python 3.7.2(default), PyAV, OpenCV, Keras, Tensorflow(CPU Mode) and other relative environment. - sunhailin-Leo/AutoConfigShellScript
* [transitive-bullshit/awesome-ffmpeg](https://github.com/transitive-bullshit/awesome-ffmpeg)  - 👻 A curated list of awesome FFmpeg resources.
* [unosquare/ffmediaelement](https://github.com/unosquare/ffmediaelement)  - FFME: The Advanced WPF MediaElement (based on FFmpeg) - unosquare/ffmediaelement
* [videomorph-dev/videomorph](https://github.com/videomorph-dev/videomorph)  - A user-friendly Video Converter based on FFMPEG and writen in Python/PyQt5. - videomorph-dev/videomorph
* [x264 FFmpeg Options Guide - Linux Encoding](https://sites.google.com/site/linuxencoding/x264-ffmpeg-mapping)  - 

## Audio
*Audio libraries, tools, and examples.*

* [Adjust and Normalize Your Music Files with FFMPEG - Make Tech Easier](https://www.maketecheasier.com/normalize-music-files-with-ffmpeg/)  - If your music files are too loud, too soft, or have obnoxious peaks and irregular volume, you can use FFmpeg to normalize your music files. Here's how.
* [Audio Loudness  |  Conversational Actions  |  Google Developers](https://developers.google.com/assistant/tools/audio-loudness)  - 
* [Audio normalization with ffmpeg using loudnorm (ebur128) filter](https://bytesandbones.wordpress.com/2017/03/16/audio-nomalization-with-ffmpeg-using-loudnorm-ebur128-filter/)  - 
* [EBU Evaluations of Multichannel Audio Codecs](https://tech.ebu.ch/docs/tech/tech3324.pdf)  - 
* [EBU R128 Introduction - Florian Camerer](https://www.youtube.com/watch?v=iuEtQqC-Sqo)  - Florian Camerer gives an introduction to the European Broadcasting Union's R128 Broadcast Standard and speaks in general about perceived loudness, peak norma...
* [How to Set Audio Levels for Video](https://www.premiumbeat.com/blog/how-to-set-audio-levels-for-video/)  - Bad sound can easily ruin good footage. Use these tips when it comes time to set audio levels for video and film projects.
* [Loudness Explained Page | Music Tribe - TC Electronic](https://www.tcelectronic.com/brand/tcelectronic/loudness-explained#googtrans(en|en))  - tcelectronic, 
* [Quick Tutorial: How to Increase Volume in Audacity [2019 Update]](https://www.iskysoft.com/video-editing/how-to-increase-volume-in-audacity.html)  - How to increase volume in Audacity? This article will guide you to change volume in Audacity and its alternative tool. You can pick up one of them to edit volume in Audacity as you like.
* [ReplayGain - Audacity Forum](https://forum.audacityteam.org/viewtopic.php?t=63067)  - 
* [Techniques for Establishing and Maintaining Audio Loudness for Digital Television](https://www.atsc.org/wp-content/uploads/2015/03/Techniques-for-establishing-and-maintaining-audio-loudness.pdf)  - 
* [bbc/audio-offset-finder: Find the offset of an audio file within another audio file](https://github.com/bbc/audio-offset-finder)  - Find the offset of an audio file within another audio file - bbc/audio-offset-finder
* [hybrik/hybrik-samples](https://github.com/hybrik/hybrik-samples/blob/master/Feature%20Examples/Filters/ebu_r128_audio_normalization.json)  - Hybrik Samples.
* [normalizing Audio](https://www.learndigitalaudio.com/normalize-audio)  - 
* [openai/jukebox](https://github.com/openai/jukebox)  - Code for the paper "Jukebox: A Generative Model for Music" - openai/jukebox
* [quodlibet/mutagen](https://github.com/quodlibet/mutagen)  - Python module for handling audio metadata. 
* [slhck/ffmpeg-normalize](https://github.com/slhck/ffmpeg-normalize#examples)  - Audio Normalization for Python/ffmpeg.
* [superpoweredSDK/Low-Latency-Android-iOS-Linux-Windows-tvOS-macOS-Interactive-Audio-Platform](https://github.com/superpoweredSDK/Low-Latency-Android-iOS-Linux-Windows-tvOS-macOS-Interactive-Audio-Platform)  - 🇸Superpowered Audio, Networking and Cryptographics SDKs. High performance and cross platform on Android, iOS, macOS, tvOS, Linux, Windows and modern web browsers. - superpoweredSDK/Low-Latency-Andr...
* [webmproject/opus-dash: Specification for Encapsulating Opus Audio in ISO-BMFF Container](https://github.com/webmproject/opus-dash)  - Specification for Encapsulating Opus Audio in ISO-BMFF Container - webmproject/opus-dash

## Subtitles and Captions
*Subtitling & Closed Caption libraries, tools, and examples.*

* [BingLingGroup/autosub](https://github.com/BingLingGroup/autosub)  - Command-line utility to transcribe/translate from video/audio/subtitles to subtitles  - BingLingGroup/autosub
* [CCExtractor/ccextractor: CCExtractor - Official version maintained by the core team](https://github.com/CCExtractor/ccextractor)  - CCExtractor - Official version maintained by the core team - CCExtractor/ccextractor
* [Can ffmpeg extract closed caption data](https://stackoverflow.com/questions/3169910/can-ffmpeg-extract-closed-caption-data)  - I am currently using ffmpeg to convert videos in various formats to flv files. One request has also come up and that is to get closed caption info out o the file as well. Does anyone have any exper...
* [Closed Captioning and Subtitling Products - MacCaption and CaptionMaker Overview - Telestream](https://www.telestream.net/captioning/overview.htm?utm_campaign=partners&utm_source=itunespartner.apple.com&utm_medium=text_link)  - Telestream Closed Captioning: MacCaption and CaptionMaker allow you to easily author, edit, create subtitles, and encode and repurpose video captions for television, web and mobile delivery
* [Comcast/caption-inspector](https://github.com/Comcast/caption-inspector)  - Caption Inspector is a reference decoder for Closed Captions (CEA-608 and CEA-708). - Comcast/caption-inspector
* [Comcast/cea-extractor](https://github.com/Comcast/cea-extractor)  - Parsing and display logic for CEA-608 caption data in fragmented MP4 files. - Comcast/cea-extractor
* [DVB captions in media convert](https://docs.aws.amazon.com/mediaconvert/latest/ug/dvb-sub-output-captions.html)  - ** If your output captions are DVB-Sub, set them up in your outputs according to the following information.
* [Dash-Industry-Forum/cea608.js](https://github.com/Dash-Industry-Forum/cea608.js)  - A JavaScript project designed to extract CEA-608 captions. - Dash-Industry-Forum/cea608.js
* [EBU-TT Live Interoperability Toolkit](http://ebu.github.io/ebu-tt-live-toolkit/)  - 
* [Eyevinn/srt-metadata-extractor](https://github.com/Eyevinn/srt-metadata-extractor)  - Contribute to Eyevinn/srt-metadata-extractor development by creating an account on GitHub.
* [IMSC 1.0.1 Text test content](https://github.com/w3c/IMSC-1.0.1_Text_TestContent/)  - 
* [IMSC 1.1 Image test content](https://github.com/w3c/IMSC-1.1_Image_TestContent/)  - 
* [IMSC 1.1 Text test content](https://github.com/w3c/IMSC-1.1_Text_TestContent/)  - 
* [IMSC HRM validator](https://github.com/sandflow/imscHRM)  - Validator for the IMSC Hypothetical Render Model (HRM), which constrains TTML document complexity
* [IMSC Specification](https://www.w3.org/TR/ttml-imsc1.1/)  - 
* [IMSC validator](https://apps.sandflow.com/imscV/)  - 
* [The ultimate guide to CCs](https://www.3playmedia.com/resources/popular-topics/closed-captioning/)  - 
* [Web Video Text Tracks Format (WebVTT)](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)  - Web Video Text Tracks Format (WebVTT) is a format for displaying timed text tracks (such as subtitles or captions) using the track element.
* [abhirooptalasila/AutoSub](https://github.com/abhirooptalasila/AutoSub)  - AutoSub is a CLI application to generate subtitle file (.srt) for any video file using Mozilla DeepSpeech - abhirooptalasila/AutoSub
* [abinashmeher999/voice-data-extract](https://github.com/abinashmeher999/voice-data-extract)  - A command line interface to combine text information from subtitles with voice data in the video. Provides a convenient way to generate training data for speech-recognition purposes. - abinashmeher...
* [active-video/subtitles](https://github.com/active-video/subtitles)  - AV Platform MPEG DASH subtitles.
* [apm1467/videocr](https://github.com/apm1467/videocr)  - Extract hardcoded subtitles from videos using machine learning - apm1467/videocr
* [awslabs/serverless-subtitles](https://github.com/awslabs/serverless-subtitles)  - Serverless Subtitles can handle a video input, extract the sound, transcript it and generate different subtitle files for your video. - awslabs/serverless-subtitles
* [cessen/subs_extract](https://github.com/cessen/subs_extract)  - Extracts per-sentence subtitles + audio from a subtitle file + video file. - cessen/subs_extract
* [federicocalendino/pysub-parser](https://github.com/federicocalendino/pysub-parser)  - Utility to extract the text and timestamps of a subtitle file (.srt, .ssa, .sub, .txt). - federicocalendino/pysub-parser
* [glut23/webvtt-py](https://github.com/glut23/webvtt-py)  - Read, write and segment WebVTT caption files in Python.
* [imscJS: IMSC/TTML/SMPTE-TT/EBU-TT-D renderer](https://github.com/sandflow/imscJS/)  - Renders IMSC/TTML/SMPTE-TT/EBU-TT-D subtitles and captions to HTML
* [jnorton001/pycaption-cli](https://github.com/jnorton001/pycaption-cli)  - A command line interface for the pycaption module. - jnorton001/pycaption-cli
* [opencoconut/webvtt-ruby](https://github.com/opencoconut/webvtt-ruby)  - WebVTT Ruby parser and segmenter.
* [osk/node-webvtt](https://github.com/osk/node-webvtt)  - Parse WebVTT files, segments and generates HLS playlists for them.
* [pbs/pycaption](https://github.com/pbs/pycaption)  - Python module to read/write popular video caption formats - pbs/pycaption
* [shawnsky/extract-subtitles](https://github.com/shawnsky/extract-subtitles)  - Extract Subtitles From Video
* [shinobizero/audio_transcriber](https://github.com/shinobizero/audio_transcriber)  - Transcodes audio & video files to text, supports MP3, M4A, WAV, MP4, MKV, AVI, MPG & MPEG. No Online API's. Python 3 - shinobizero/audio_transcriber
* [smacke/subsync](https://github.com/smacke/subsync)  - Automagically synchronize subtitles with video.
* [statsbiblioteket/tv-subtitle-extraction](https://github.com/statsbiblioteket/tv-subtitle-extraction)  - System for extraction of subtitles from TV broadcasts. - statsbiblioteket/tv-subtitle-extraction
* [szatmary/libcaption](https://github.com/szatmary/libcaption)  - Free open-source CEA608 / CEA708 closed-caption encoder/decoder - szatmary/libcaption
* [ttconv: subtitle/caption format converter](https://github.com/sandflow/ttconv)  - Converts EBU STL, IMSC/TTML/SMPTE-TT/EBU-TT-D and 608/SCC into IMSC, WebVTT and SRT
* [wargarblgarbl/libgosubs](https://github.com/wargarblgarbl/libgosubs)  - 
* [xinnjie/extract-subtitle](https://github.com/xinnjie/extract-subtitle)  - extract subtitles from video.

## Dubbing

*Automatic dubbing systems*

* [jordimas/open-dubbing](https://github.com/jordimas/open-dubbing) - Open dubbing is an AI dubbing system uses machine learning models to automatically translate and synchronize audio dialogue into different languages.

## Ads
*Ads in streaming video related libraries, tools, examples, and resources.*

* [Eyevinn/adxchange-engine](https://github.com/Eyevinn/adxchange-engine)  - Eyevinn Adxchange Engine is a microservice placed between the server-side ad-insertion component and the adserver or SSP - Eyevinn/adxchange-engine
* [Eyevinn/vast-info](https://github.com/Eyevinn/vast-info)  - Parse a VAST or VMAP to show valuable information in a readable format - Eyevinn/vast-info
* [Eyevinn/vmapproxy](https://github.com/Eyevinn/vmapproxy)  - A simple VMAP / VAST proxy. 
* [OpenVisualCloud/Ad-Insertion-Sample](https://github.com/OpenVisualCloud/Ad-Insertion-Sample)  - The ad-insertion reference pipeline shows how to integrate various media building blocks, with analytics powered by the OpenVINO™ Toolkit, for intelligent server-side ad insertion. - OpenVisualClou...
* [SCTE-104/35 and Beyond: A Look at Ad Insertion in an OTT World](https://www.tvtechnology.com/opinions/scte10435-and-beyond-a-look-at-ad-insertion-in-an-ott-world)  - Ad Insertion is a very important part of many video delivery systems because of the monetization aspect—it generates revenue!
* [Understanding Real-time Bidding for AVOD Services](https://medium.com/@eyevinntechnology/understanding-real-time-bidding-for-avod-services-861ebfa8bd13)  - We have in previous blog articles described the principles behind server-side ad-insertion and described some of the challenges with it as…
* [Understanding Server-Side Dynamic Ad Insertion](https://medium.com/@eyevinntechnology/understanding-server-side-dynamic-ad-insertion-d7ed90e34aa2)  - In this post we’re explaining the principles behind Server-Side Dynamic Ad Insertion technology. If you are already familiar with video…
* [erikkaashoek/Comskip](https://github.com/erikkaashoek/Comskip)  - A free commercial detector. 

## Vendors
*Video indurstry's various vendors products and documentations.*

* [switch media adease](https://www.switch.tv/mediahq/adease/)  - 
* [switch media live2vod](https://www.switch.tv/mediahq/live2vod/)  - 
* [switch media mediahq](https://www.switch.tv/mediahq/)  - 
* [switch media universal player](https://www.switch.tv/mediahq/universal-player/)  - 

### Dolby
*Dolby specs, libraries, examples, and tools.*
[back to top](#readme) 

* [Dolby Vision for Content Creators | Dolby Laboratories](https://www.dolby.com/us/en/technologies/dolby-vision/dolby-vision-for-creative-professionals.html)  - The Dolby Vision integrated workflow gives you the tools needed to efficiently create wide color gamut and high dynamic range content and ensures that the look you create in the color suite stays true when experienced across across a multitude of devices. With Dolby Vision high dynamic range imaging, you get bolder highlights and incredible contrast. That means greater sharpness, depth, and more detailed shadows to expand your storytelling possibilities like never before.
* [DolbyLaboratories/AM-Viewer: Audio Metadata Viewer](https://github.com/DolbyLaboratories/AM-Viewer)  - Audio Metadata Viewer. Contribute to DolbyLaboratories/AM-Viewer development by creating an account on GitHub.
* [DolbyLaboratories/dbmd-atmos-parser: Dolby Atmos DBMD Wave Chunk Parser](https://github.com/DolbyLaboratories/dbmd-atmos-parser)  - Dolby Atmos DBMD Wave Chunk Parser. Contribute to DolbyLaboratories/dbmd-atmos-parser development by creating an account on GitHub.
* [DolbyLaboratories/dlb_mp4base: The Dolby MP4 streaming muxer (dlb_mp4base) is a software implementation of a muxer of fragmented or unfragmented ISO base media file format (mp4). It supports muxing of Dolby Digital (AC-3), Dolby Digital Plus (E-AC-3), and](https://github.com/DolbyLaboratories/dlb_mp4base)  - The Dolby MP4 streaming muxer (dlb_mp4base) is a software implementation of a muxer of fragmented or unfragmented ISO base media file format (mp4). It supports muxing of Dolby Digital (AC-3), Dolby...
* [DolbyLaboratories/dolby_vision_professional_decoder_plugin](https://github.com/DolbyLaboratories/dolby_vision_professional_decoder_plugin)  - 
* [DolbyLaboratories/pmd_tool: pmd_tool is a command line utility that converts between different representations of SMPTE RDD49 metadata](https://github.com/DolbyLaboratories/pmd_tool)  - pmd_tool is a command line utility that converts between different representations of SMPTE RDD49 metadata - DolbyLaboratories/pmd_tool
* [Hybrik API Reference](https://docs.hybrik.com/api/v1/HybrikAPI.html?#getting-started)  - 
* [ShaoWeiguo/dlb_mp4demux: The Dolby MP4 streaming demuxer (dlb_mp4demux) is a software implementation of a demuxer of fragmented or unfragmented ISO base media file format (mp4). It supports demuxing of Dolby Digital (AC-3), Dolby Digital Plus (E-AC-3), an](https://github.com/ShaoWeiguo/dlb_mp4demux)  - The Dolby MP4 streaming demuxer (dlb_mp4demux) is a software implementation of a demuxer of fragmented or unfragmented ISO base media file format (mp4). It supports demuxing of Dolby Digital (AC-3)...
* [dolby-encoding-engine/plugins at master · DolbyLaboratories/dolby-encoding-engine](https://github.com/DolbyLaboratories/dolby-encoding-engine/tree/master/plugins)  - Contribute to DolbyLaboratories/dolby-encoding-engine development by creating an account on GitHub.
* [hybrik/hybrik-samples](https://github.com/hybrik/hybrik-samples)  - Hybrik Samples.

## QoE
*QoE & Analytics tools, libraries, and resources.*

* [Best Practices for End-to-End Workflow Monitoring | Streaming Video Alliance](https://www.streamingvideoalliance.org/project/best-practices-for-end-to-end-workflow-monitoring/)  - 
* [Collection of VMAF Resources](https://streaminglearningcenter.com/blogs/collection-of-vmaf-resources.html)  - A colleague asked for some resources relating to VMAF. Rather than answer in an email I thought I would create a post around it. Some of these are from Netflix, most from me (Jan Ozer). I’ve broken the items into three groups; Computing VMAF, Using VMAF, and About VMAF. I hope you find this collection useful.…
* [JNoDuq/videobench](https://github.com/JNoDuq/videobench)  - VMAF PSNR Bitrate Analyzer.
* [MarcAntoine-Arnaud/wisual](https://github.com/MarcAntoine-Arnaud/wisual)  - Web for Visual Quality Assessment. 
* [Netflix/vmaf](https://github.com/Netflix/vmaf/)  - Perceptual video quality assessment based on multi-method fusion. - Netflix/vmaf
* [QCTools Documentation](http://bavc.github.io/qctools/)  - QCTools (Quality Control Tools for Video Preservation) is a free and open source software tool that helps users analyze and understand their digitized video files through use of audiovisual analytics and filtering. QCTools is funded by the National Endowment for the Humanities and the Knight Foundation, and is developed by the Bay Area Video Coalition.
* [Quality of Experience in Streaming](https://medium.com/@eyevinntechnology/quality-of-experience-in-streaming-5c25355a4111?source=userActivityShare-94bccb50d11-1559724940&_branch_match_id=664741478927428385)  - In Eyevinn Technology’s ambition to broader our sharing of knowledge we now expand this with addressing quality. In today’s landscape of…
* [Rolinh/VQMT](https://github.com/Rolinh/VQMT)  - VQMT: Video Quality Measurement Tool. Fast implementations of the following objective image quality metrics: PSNR, SSIM, MS-SSIM, VIFp, PSNR-HVS and PSNR-HVS-M. - Rolinh/VQMT
* [Telecommunication-Telemedia-Assessment/AVRate](https://github.com/Telecommunication-Telemedia-Assessment/AVRate)  - An open source modular Audio/Visual subjective evaluation test interface - Telecommunication-Telemedia-Assessment/AVRate
* [The Challenge to Maintain and Translate Creative Visual Ideas to Everyone’s Viewing Devices](https://medium.com/@eyevinntechnology/the-challenge-to-maintain-and-translate-creative-visual-ideas-to-everyones-viewing-devices-a88e1a841439)  - Many articles have already been posted drawing conclusions on what went wrong with the visual quality of a very popular TV show that was…
* [Toward A Practical Perceptual Video Quality Metric](https://medium.com/netflix-techblog/toward-a-practical-perceptual-video-quality-metric-653f208b9652)  - measuring video quality accurately at scale
* [VMAF: The Journey Continues](https://medium.com/netflix-techblog/vmaf-the-journey-continues-44b51ee9ed12)  - by Zhi Li, Christos Bampis, Julie Novak, Anne Aaron, Kyle Swanson, Anush Moorthy and Jan De Cock
* [VQEG Tools and Subjective Labs Setup](https://vqeg.github.io/software-tools/)  - Providing the video quality research community with a wide variety of software tools and guidance in order to facilitate research.
* [VQEG/software-tools](https://github.com/VQEG/software-tools)  - VQEG's Software and Tools Website. 
* [Video Bench — How measure your video quality easily](https://medium.com/@jnoduq/video-bench-how-measure-your-video-quality-easily-85a0feb8f6e2)  - Introduction
* [Video Quality Assessment](https://medium.com/@eyevinntechnology/video-quality-assessment-34abd35f96c0?source=userActivityShare-94bccb50d11-1560983815&_branch_match_id=670021582869771680)  - In Eyevinn’s initiative to share our knowledge around quality we continue with addressing video quality assessment; from both a subjective…
* [Video Quality Experts Group (VQEG)](https://www.its.bldrdoc.gov/vqeg/vqeg-home.aspx)  - 
* [bavc/qctools](https://github.com/bavc/qctools)  - 
* [crunchyroll/objective_perceptual_analysis](https://github.com/crunchyroll/objective_perceptual_analysis)  - 
* [cta-wave/R4WG20-QoE-Metrics](https://github.com/cta-wave/R4WG20-QoE-Metrics)  - Issue tracking repository for the R4-Wg20 QoE Initiative - cta-wave/R4WG20-QoE-Metrics
* [gdavila/easyVmaf](https://github.com/gdavila/easyVmaf)  - Python script to easily compute VMAF using FFmpeg. It allows to deinterlace, scale and sync Ref and Distorted video automatically - gdavila/easyVmaf

## Tools
*Streaming video tools and resources to make life easier.*

* [A Docker container with the video streaming tools you need](https://medium.com/@eyevinntechnology/a-docker-container-with-the-video-streaming-tools-you-need-b8319e98f36a)  - As a video streaming technician there are a number of tools that you find yourself using on a daily basis. Wouldn’t it be handy if all…
* [Comcast/eel](https://github.com/Comcast/eel)  - A simple proxy service to forward JSON events and transform or filter them along the way. - Comcast/eel
* [Comcast/gots](https://github.com/Comcast/gots)  - MPEG Transport Stream handling in Go.
* [Comcast/mamba](https://github.com/Comcast/mamba)  - Mamba is a Swift iOS, tvOS and macOS framework to parse, validate and write HTTP Live Streaming (HLS) data. - Comcast/mamba
* [Comcast/scte35-js](https://github.com/Comcast/scte35-js)  - A SCTE 35 Parser for JavaScript.
* [DSRCorporation/imf-conversion](https://github.com/DSRCorporation/imf-conversion)  - NF IMF media conversion utility allows to handle flat file creation from a specified CPL within the IMF package - DSRCorporation/imf-conversion
* [Eyevinn/channel-engine](https://github.com/Eyevinn/channel-engine)  - OTT TV Channel Engine.
* [Eyevinn/docker-jit-capture](https://github.com/Eyevinn/docker-jit-capture)  - A Docker container for an open source Just-In-Time Capture Origin - Eyevinn/docker-jit-capture
* [Eyevinn/docker-serve](https://github.com/Eyevinn/docker-serve)  - A simple Python based HTTP server that sets CORS allow headers. Useful for streaming from files on local computer - Eyevinn/docker-serve
* [Eyevinn/fmp4-js](https://github.com/Eyevinn/fmp4-js)  - A Javascript library to parse ISO Base Media File Format (MPEG-4 Part 12) - Eyevinn/fmp4-js
* [Eyevinn/pseudo-live-playout](https://github.com/Eyevinn/pseudo-live-playout)  - Contribute to Eyevinn/pseudo-live-playout development by creating an account on GitHub.
* [Eyevinn/toolbox](https://github.com/Eyevinn/toolbox)  - A set of Docker containers with Streaming tools.
* [IENT/YUView](https://github.com/IENT/YUView)  - YUView is a QT based, cross-platform YUV player with an advanced analytic toolset.
* [Inca — Message Tracing and Loss Detection For Streaming Data @Netflix](https://link.medium.com/Lu3GnIPeg0)  - At Netflix, our real-time data infrastructure have embraced the multi-cluster Kafka architecture and Flink powered stream processing…
* [Kthulu120/liquid_dl](https://github.com/Kthulu120/liquid_dl)  - Liquid-dl is a simple tool for utlities such as FFMPEG, youtube-dl, and scdl. It provides a simple framework with simple point and click options allowing users to just click on what they need and u...
* [Marcos-A/STRCleaner](https://github.com/Marcos-A/STRCleaner)  - Script that extracts all the text from a subtitles file ignoring time indications, HTML tags and other alien info. - Marcos-A/STRCleaner
* [MediaArea/MediaInfo](https://github.com/MediaArea/MediaInfo)  - Convenient unified display of the most relevant technical and tag data for video and audio files. - MediaArea/MediaInfo
* [Open Broadcaster Software | OBS](https://obsproject.com/)  - OBS (Open Broadcaster Software) is free and open source software for video recording and live streaming. Stream to Twitch, YouTube and many other providers or record your own videos with high quality H264 / AAC encoding.
* [Shaka Packager – opensource.google](https://opensource.google/projects/shaka-packager)  - Learn about all our projects.
* [Stream Analyzer - ts analyzer, stream validation, ETSI TR 101 290 | Elecard: Video Compression Guru ](https://www.elecard.com/products/video-analysis/stream-analyzer)  - Professional Video Analysis Tool For Syntax Analysis Of Encoded Media Streams. Operates With MPEG-2 PS/TS, VES and MP4 Files. Automation, batch execution via Command Line Interface. Check your multiplexer
* [Streamlab](https://vimond.github.io/streamlab/)  - Multi-format stream test tool for the browser. Brings convenience to verifying, inspecting, and troubleshooting adaptive streams and video files. A common interface on top of Shaka Player, HLS.js, and Rx-Player.
* [The Top 656 Video Open Source Projects](https://awesomeopensource.com/projects/video)  - Browse The Most Popular 656 Video Open Source Projects
* [VTCLab Media Analyzer](https://media-analyzer.pro)  - In-browser tool that helps to analyze the internal structure of MPEG-TS and MP4/MOV files
* [ZaifSenpai/Batch-Py-Remux](https://github.com/ZaifSenpai/Batch-Py-Remux)  - Convert mkv video to hevc (h.265).
* [antiboredom/videogrep](https://github.com/antiboredom/videogrep)  - automatic video supercuts with python. 
* [awslabs/aws-stale-playlist-detector](https://github.com/awslabs/aws-stale-playlist-detector)  - The Stale Playlist Detector (SPD) is a tool to monitor live HLS origin endpoints for changing playlists. The Stale Playlist Detector (SPD) will use data in the top-level playlist, the child playlis...
* [bcpierce00/unison](https://github.com/bcpierce00/unison)  - Unison file synchronizer.
* [brendanlong/mpeg-ts-inspector: A command-line tool for inspecting MPEG-TS files](https://github.com/brendanlong/mpeg-ts-inspector)  - A command-line tool for inspecting MPEG-TS files. Contribute to brendanlong/mpeg-ts-inspector development by creating an account on GitHub.
* [coopernurse/nginx-s3-proxy](https://github.com/coopernurse/nginx-s3-proxy)  - nginx compiled with aws-auth support, suitable for S3 reverse proxy usage - coopernurse/nginx-s3-proxy
* [ebu/content-manager](https://github.com/ebu/content-manager)  - The Content Manager is a visual production tool which is able to generate on the fly visualisation for DAB slideshow and RadioVIS. .NET framework based, it is developed in C# and is distributed und...
* [egg-bread/hls-to-mp4](https://github.com/egg-bread/hls-to-mp4)  - Download HLS videos as MP4 (WebVTT for caption download optional) - egg-bread/hls-to-mp4
* [essential61/mp4analyser](https://github.com/essential61/mp4analyser)  - mp4 file analyser written in Python. 
* [estliberitas/node-thumbnails-webvtt](https://github.com/estliberitas/node-thumbnails-webvtt)  - Video thumbnail generator generating WebVTT spec file - estliberitas/node-thumbnails-webvtt
* [excalibur-kvrv/m3u8-dl](https://github.com/excalibur-kvrv/m3u8-dl)  - A CLI m3u8-downloader program to parse .m3u8 playlist file and download mpeg2-ts video files, concat them and convert it to mp4 using FFMPEG - excalibur-kvrv/m3u8-dl
* [flavioribeiro/video-thumbnail-generator](https://github.com/flavioribeiro/video-thumbnail-generator)  - :camera: Generate thumbnail sprites from videos. 
* [gnolizuh/BLSS](https://github.com/gnolizuh/BLSS)  - NGINX-based Live Media Streaming Server.
* [gpac/gpac](https://github.com/gpac/gpac)  - GPAC main code repository.
* [gpac/mp4box.js](https://github.com/gpac/mp4box.js)  - JavaScript version of GPAC's MP4Box tool.
* [huzhenjie/m3u8_downloader](https://github.com/huzhenjie/m3u8_downloader)  - 基于Python的m3u8下载器. 
* [ilstam/FF-Multi-Converter: GUI File Format Converter](https://github.com/ilstam/FF-Multi-Converter)  - GUI File Format Converter. Contribute to ilstam/FF-Multi-Converter development by creating an account on GitHub.
* [jamesfining/scte](https://github.com/jamesfining/scte)  - Python library to work with SCTE standards. 
* [jkarthic-akamai/ABR-Broadcaster](https://github.com/jkarthic-akamai/ABR-Broadcaster)  - A real time encoder for Adaptive Bitrate Broadcast - jkarthic-akamai/ABR-Broadcaster
* [jordicenzano/go-ts-segmenter](https://github.com/jordicenzano/go-ts-segmenter)  - Live TS segmenter and HLS manifest creation in Go. 
* [justdan96/tsMuxer](https://github.com/justdan96/tsMuxer)  - tsMuxer is a transport stream muxer for remuxing/muxing elementary streams, EVO/VOB/MPG, MKV/MKA, MP4/MOV, TS, M2TS to TS to M2TS. Supported video codecs H.264/AVC, H.265/HEVC, VC-1, MPEG2. Support...
* [liwf616/awesome-live-stream](https://github.com/liwf616/awesome-live-stream)  - Webrtc && Nginx && DASH && Quic 学习资料收集，持续更新中.
* [mar10/wsgidav](https://github.com/mar10/wsgidav)  - A generic and extendable WebDAV server based on WSGI - mar10/wsgidav
* [mifi/lossless-cut](https://github.com/mifi/lossless-cut)  - 
* [minio/minio](https://github.com/minio/minio)  - MinIO is a high performance object storage server compatible with Amazon S3 APIs - minio/minio
* [mrpdaemon/mmf](https://github.com/mrpdaemon/mmf)  - Video transcoding ffmpeg frontend in Python. 
* [obsproject/obs-studio](https://github.com/obsproject/obs-studio)  - OBS Studio - Free and open source software for live streaming and screen recording - obsproject/obs-studio
* [realeyes-media/alpine-bento-ffmpeg](https://github.com/realeyes-media/alpine-bento-ffmpeg)  - Alpine Linux with FFMPEG, Bento, and PM2.
* [realeyes-media/alpine-node-video-multitool](https://github.com/realeyes-media/alpine-node-video-multitool)  - Contribute to realeyes-media/alpine-node-video-multitool development by creating an account on GitHub.
* [sannies/isoviewer: GUI application to have closer look ISO 14496-12 and other MP4 files.](https://github.com/sannies/isoviewer)  - GUI application to have closer look ISO 14496-12 and other MP4 files. - sannies/isoviewer
* [sannies/mp4parser: A Java API to read, write and create MP4 files](https://github.com/sannies/mp4parser)  - A Java API to read, write and create MP4 files. Contribute to sannies/mp4parser development by creating an account on GitHub.
* [sbraz/pymediainfo: A Python wrapper around the MediaInfo library](https://github.com/sbraz/pymediainfo)  - A Python wrapper around the MediaInfo library. Contribute to sbraz/pymediainfo development by creating an account on GitHub.
* [schedules/dl](https://github.com/schedules/dl)  - Node.js DASH and HLS downloader. 
* [slhck/ffmpeg-bitrate-stats](https://github.com/slhck/ffmpeg-bitrate-stats)  - Calculate bitrate statistics using FFmpeg
* [slhck/ffmpeg-debug-qp](https://github.com/slhck/ffmpeg-debug-qp)  - FFmpeg Debug Script for QP Values
* [slhck/ffmpeg-quality-metrics](https://github.com/slhck/ffmpeg-quality-metrics)  - Calculate quality metrics with FFmpeg (SSIM, PSNR, VMAF)
* [slhck/scenecut-extractor](https://github.com/slhck/scenecut-extractor)  - Extract scenecuts from video files using ffmpeg
* [vapoursynth/vapoursynth](https://github.com/vapoursynth/vapoursynth)  - A video processing framework with simplicity in mind - vapoursynth/vapoursynth
* [video-dev/vtt.js](https://github.com/video-dev/vtt.js)  - A JavaScript implementation of the WebVTT specification - video-dev/vtt.js
* [watson-developer-cloud/text-to-speech-nodejs](https://github.com/watson-developer-cloud/text-to-speech-nodejs)  - :speaker: Sample Node.js Application for the IBM Watson Text to Speech Service - watson-developer-cloud/text-to-speech-nodejs
* [xk media library](https://github.com/chapmanjacobd/library)  - Scan millions of files with ffmpeg and access the metadata as a SQLite database. Also, a CLI alternative to media browsers like Plex or Jellyfin

## DRM
*DRM tools, documentations, and resources.*

* [Advanced Encryption Techniques: ContentProtection Tags for MPDs and PSSH Boxes for DASH.](https://go.buydrm.com/thedrmblog/advanced_encryption_techniques)  - In this installment of TheDRMBlog we take an in-depth look at Advanced Encryption Techniques.
* [Axinom/cpix-validator: Web app for validating CPIX documents](https://github.com/Axinom/cpix-validator)  - Web app for validating CPIX documents. Contribute to Axinom/cpix-validator development by creating an account on GitHub.
* [Binary to base64: Convert between bytes and base64 — Cryptii](https://cryptii.com/pipes/binary-to-base64)  - Base64 encoding schemes are used when binary data needs to be stored or transferred as textual data. Therefore 64 characters are chosen that are both members of a subset common to most encodings (ASCII), and also printable.
* [BuyDRM_KeyOS_PlatformOverview_FUUGO_062118](https://go.buydrm.com/hubfs/BuyDRM_KeyOS_Content_Protection_in_DASH_DASHIF_Workshop_Comcast_August2018-1.pdf)  - 
* [Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/#search=drm)  - 
* [Content Protection for HLS with AES-128 Encryption](https://www.theoplayer.com/blog/content-protection-for-hls-with-aes-128-encryption)  - We will outline the most popular method for content protection with the HTTP Live Streaming (HLS) protocol: AES-128 content encryption.
* [CrackerCat/video_decrypter](https://github.com/CrackerCat/video_decrypter)  - Decrypt video from a streaming site with MPEG-DASH Widevine DRM encryption. - CrackerCat/video_decrypter
* [Creating a secure video-on-demand (VOD) platform using AWS](https://aws.amazon.com/blogs/media/creating-a-secure-video-on-demand-vod-platform-using-aws/)  - Authored by Chirag Oswal, Solution Architect, AWS, and Vikas Tiwari, Solution Architect Manager, AWS Video has become the primary means of Information sharing and learning. Customers are investing in innovative solutions to tap into the e-learning and video space. Video content is their IP and needs to be protected and securely delivered. Online video is a […]
* [Deploying KeyOS with AWS Elemental Media Services](https://go.buydrm.com/thedrmblog/deploying-keyos-with-aws-elemental-media-services)  - In this post we provide an in-depth first party overview of the complex integration between the KeyOS Platform and the Elemental Media Services via the SPEKE API.
* [Digital Rights Management (DRM) – Everything you need to know](https://bitmovin.com/digital-rights-management-everything-to-know/)  - 
* [Digital Rights Management (multi - drm) – aameer.github.io](https://aameer.github.io/articles/digital-rights-management-multi-drm)  - My Site
* [Encryption & DRM with Multiple Keys — Unified Streaming](https://docs.unified-streaming.com/documentation/package/multiple-keys.html)  - DRM with multiple keys for Unified Packager
* [Fyrd/caniuse](https://github.com/Fyrd/caniuse)  - Raw browser/feature support data from caniuse.com. 
* [Generate MPEG DASH content encrypted with MPEG CENC ClearKey · Dash-Industry-Forum/dash.js Wiki](https://github.com/Dash-Industry-Forum/dash.js/wiki/Generate-MPEG-DASH-content-encrypted-with-MPEG-CENC-ClearKey)  - A reference client implementation for the playback of MPEG DASH via Javascript and compliant browsers. - Dash-Industry-Forum/dash.js
* [HEVC DRM Market Update](https://go.buydrm.com/thedrmblog/hevc-drm-market-update)  - Since time eternal, the streaming industry has toiled with and extolled the virtues of CODECs and their key enablement of the entire digital video experience. Now comes the latest candy in the increasingly large bowl, H.265 (MPEG-H Part 2) or as it’s more commonly known. HEVC.
* [HLS with Widevine for Android - Taku Semba - Medium](https://medium.com/@takusemba/hls-with-widevine-for-android-de3f41027ed2)  - As of the version of 2.6.0, ExoPlayer started supporting Widevine + HLS playback. WideVine is the one of the DRM schemes defined by Google…
* [How to Protect Your Content With DRM](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=132289&pageNum=2)  - Lock it down. If you're streaming proprietary or premium online video, it's time to take the step up to true digital rights management protection. Here's how to get started.
* [Integrate BuyDRM for a Multi-DRM workflow](https://bitmovin.com/integrate-buydrm-multi-drm-system)  - 
* [Microsoft Word - EZDRM Bento 4 Open Source.docx](https://www.ezdrm.com/Documentation/EZDRM%20Bento%204%20Open%20Source%20v1.0.pdf)  - 
* [Play your own DRM content on ExoPlayer - Taku Semba - Medium](https://medium.com/@takusemba/play-your-own-drm-content-on-exoplayer-e8ed73d5864c)  - Digital rights management, or you could just refer to it as DRM, is a way of controlling what users can do with some sort of digital…
* [Pssh box](https://raw.githubusercontent.com/google/shaka-packager/master/packager/tools/pssh/pssh-box.py)  - 
* [Secure HLS streaming using DRM encryption](https://www.wowza.com/docs/how-to-secure-apple-hls-streaming-using-drm-encryption)  - Protect live and on-demand HLS streaming using DRM encryption in Wowza Streaming Engine.
* [Securing OTT Content — DRM](https://medium.com/@eyevinntechnology/securing-ott-content-drm-1af2c08fdd31?source=userActivityShare-94bccb50d11-1560983518&_branch_match_id=670020366479331042)  - Written by: Boris Asadanin, Streaming Media Consultant and Partner at Eyevinn Technology
* [The Hitchhiker's Guide to DRM](https://ottverse.com/hitchhikers-guide-to-drm-2/)  - A gentle guide to the world of Digital Rights Management. It includes a technology overview of AES, EME, CDM, CENC, Keys, and then explores popular DRM technologies such as Google Widevine, Apple FairPlay, Microsoft PlayReady, and finally, Multi-DRM.
* [TheDRMBlog | CENC](https://go.buydrm.com/thedrmblog/topic/cenc)  - CENC | The DRM Blog - Your New Official Source for Everything DRM
* [castlabs/dashencrypt: DASH fragmenter/segmenter and encrypter](https://github.com/castlabs/dashencrypt)  - DASH fragmenter/segmenter and encrypter. Contribute to castlabs/dashencrypt development by creating an account on GitHub.
* [draft-pantos-hls-rfc8216bis-00 - HTTP Live Streaming 2nd Edition](https://tools.ietf.org/html/draft-pantos-hls-rfc8216bis-00#section-5.1)  - 
* [shengbinmeng/dash-drm](https://github.com/shengbinmeng/dash-drm)  - Demos of MPEG-DASH and DRM.
* [videojs/aes-decrypter](https://github.com/videojs/aes-decrypter)  - Contribute to videojs/aes-decrypter development by creating an account on GitHub.
* [w3c/encrypted-media](https://github.com/w3c/encrypted-media/)  - Encrypted Media Extensions. 

## Testing
*Video streaming testing tools and helpers.*

* [4K Media | Free Ultra-HD / HDR / HLG / Dolby Vision 4K Video Demos](https://4kmedia.org/)  - Uncompressed 4K demos, samples, and trailers, to show off your new ultra-HD (2160p) HDR/HLG/Dolby Vision television or monitor.
* [Automated Testing on Devices](https://medium.com/netflix-techblog/automated-testing-on-devices-fc5a39f47e24)  - key concepts and infrastructure
* [DASH & HLS Sample Streams](https://bitmovin.com/mpeg-dash-hls-examples-sample-streams/)  - 
* [HTTP Live Streaming (HLS) - Artillery.io Docs](https://artillery.io/docs/plugin-hls/)  - 
* [MPEG DASH Sample Content | Bento4](http://www.bento4.com/developers/dash/dash-sample-content)  - 
* [Xiph.org :: Test Media](https://media.xiph.org/)  - 
* [artilleryio/artillery-plugin-hls](https://github.com/artilleryio/artillery-plugin-hls)  - Load test HTTP Live Streaming (HLS) servers with Artillery 🎥 - artilleryio/artillery-plugin-hls
* [bengarney/list-of-streams](https://github.com/bengarney/list-of-streams)  - Community list of public test streams for HLS and DASH. - bengarney/list-of-streams
* [ebu/test-engine-live-tools](https://github.com/ebu/test-engine-live-tools)  - Small tools and scripts for the EBU test engine platform. - ebu/test-engine-live-tools
* [ebu/test-engine-ondemand](https://github.com/ebu/test-engine-ondemand)  - EBU on-demand test engine. 
* [video-dev/streams](https://github.com/video-dev/streams)  - A repository of shared streams - no media uploads.

## Community
*Video developers community, slack groups, conferences, meetups*

* [Community events of the VideoLAN non-profit organization](https://www.videolan.org/videolan/events)  - VideoLAN events

### Conferences
[back to top](#readme) 


### Meet ups
[back to top](#readme) 


### Slack Groups
[back to top](#readme) 


## CDN
*Last mile tools, documentations, and resources.*

* [AWS CloudFront Live failover](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html)  - You can set up CloudFront with origin failover for scenarios that require high availability. To get started, create an origin group in which you designate a primary origin for CloudFront plus a second origin that CloudFront automatically switches to when the primary origin returns specific HTTP status code failure responses.
* [AWS CloudFront for Live Streaming](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/live-streaming.html)  - To use AWS Media Services with CloudFront to deliver live content to a global audience, follow the guidance included in this section.
* [Amazon S3 | Fastly Help Guides](https://docs.fastly.com/en/guides/amazon-s3)  - 
* [Edge Computing with Fastly CDN and Varnish VCL for Authenticated Requests - Endertech](https://endertech.com/blog/edge-computing-fastly-cdn-varnish-vcl-authenticated-requests)  - A brief explanation of how to use Fastly CDN and Varnish with authenticated requests to offload static file serving from the origin and edge caching.
* [Lambda Edge Tutorial](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works-tutorial.html)  - This tutorial shows you how to get started with Lambda@Edge by helping you create and add a sample Node.js function that runs in CloudFront. The example that we walk through adds HTTP security headers to a response, which can improve security and privacy for a website. (That said, you don’t need a website for this walkthrough; we simply add security headers to a response when CloudFront retrieves a file.)
* [Lambda@Edge Design Best Practices | Amazon Web Services](https://aws.amazon.com/blogs/networking-and-content-delivery/lambdaedge-design-best-practices/)  - Lambda@Edge transforms CloudFront into a highly programmable CDN with serverless compute capabilities closer to your viewers around the world. This blog is the first in a series that explains best practices associated with using Lambda@Edge functions to customize your content delivery.
* [OTT Content Delivery– CDN Alternatives](https://medium.com/@eyevinntechnology/ott-content-delivery-cdn-alternatives-cafe75dab71d?source=userActivityShare-94bccb50d11-1560983135&_branch_match_id=670018733519578135)  - Introduction

## HDR10, HLG, Dolby Vision
*HDR tools, learning, documentations, and resources.*

* [Dolby Stream Validator](https://ott.dolby.com/OnDelKits_dev/StreamValidator/Start_Here.html)  - 
* [Encode HDR with VP9](https://developers.google.com/media/vp9/hdr-encoding)  - Hands on tutorial of using ffmpeg to do hdr encoding
* [Frequently Asked Questions on High Dynamic Range and Hybrid Log-Gamma](https://downloads.bbc.co.uk/rd/pubs/papers/HDR/BBC_HDRTV_FAQ.pdf)  - FAQ regarding HDR by BBC R&D
* [HLG vs PQ Systems for HDR Television](https://www.displaydaily.com/article/display-daily/hlg-vs-pq-systems-for-hdr-television)  - Article explaining hlg vs pq in depth.
* [High Dynamic Range Television and Hybrid Log-Gamma - BBC R&D](https://www.bbc.co.uk/rd/projects/high-dynamic-range)  - BBC R&D HDR project page.
* [Use of Look-Up Tables (LUTs) in FFmpeg](https://downloads.bbc.co.uk/rd/pubs/papers/HDR/BBC_HDRTV_Use_of_LUTs_FFmpeg.pdf)  - How to use luts with ffmpeg for converting between differnt hdr encodes
* [Vittorio Giovara - Color Me Intrigued: A Jaunt Through Color Technology in Video](https://www.youtube.com/watch?v=XMnvY7a4-As&feature=share)  - This talk aims to shed light on colorspaces - what they are, how and why they work, why we should care about handling edge cases properly. Starting with hist...
* [bbc/qtff-parameter-editor](https://github.com/bbc/qtff-parameter-editor)  - QuickTime file parameter editor for modifying transfer function, colour primary and matrix characteristics.
* [id3as/ffmpeg-libvpx-HDR-static](https://github.com/id3as/ffmpeg-libvpx-HDR-static)  - A script to build a static binary of FFmpeg optimised for libvpx (HDR 10bit) encoding.


### Contributing

Please take a quick look at the [contribution guidelines](https://github.com/krzemienski/awesome-video/blob/master/.github/CONTRIBUTING.md) first. If you see a package or project here that is no longer maintained or is not a good fit, please submit a pull request to improve this file. Thank you to all [contributors](https://github.com/krzemienski/awesome-video/graphs/contributors); you rock!!
