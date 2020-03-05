# Awesome Video [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
 
<!-- 

PLEASE DO NOT UPDATE THIS FILE, UPDATE CONTENTS.JSON INSTEAD. THANK YOU :-)

 -->





### Contents

- [Introduction](#intro)
- [Learning](#learning)
  - [Books](#books)
  - [Talks Presentations Podcasts](#talks-presentations-podcasts)
- [HLS](#hls)
- [DASH](#dash)
- [Encoding](#encoding)
  - [AV1](#av1)
  - [HEVC](#hevc)
  - [VP9](#vp9)
- [Streaming Server and Storage](#streaming-server-and-storage)
- [Reading](#reading)
- [Specs and Standards](#specs-and-standards)
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
* [leandromoreira/digital_video_introduction](https://github.com/leandromoreira/digital_video_introduction)  - A hands-on introduction to video technology: image, video, codec (av1, vp9, h265) and more (ffmpeg encoding). - leandromoreira/digital_video_introduction

## Learning
*An awesome list of learning video streaming resources.*

* [Adding Alternate Media to a Playlist | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/adding_alternate_media_to_a_playlist)  - 
* [Back to Basics: Encoding Definition and Adaptive Bitrate](https://bitmovin.com/encoding-definition-bitrates/?utm_campaign=Newsletter&utm_medium=email&_hsenc=p2ANqtz-8MPFxhR7snQrxPYM7Bl3UTEMgOh5ZXoDQCHjLl9lkskqE0IfBhEuz3us39Br-lvA_CnyNmQl6L5wqO6iKOfAJ8HznenQ&_hsmi=79678208&utm_content=79677632&utm_source=hs_email&hsCtaTracking=b8eb0e0a-f292-435e-8b99-719b75d81412%7C367afa65-d810-4c2e-aa2c-c87e897a8942)  - 
* [Create your own video streaming server with Linux](https://opensource.com/article/19/1/basic-live-video-streaming-server)  - Live video streaming is incredibly popular—and it's still growing. Platforms like Amazon's Twitch and Google's YouTube boast millions of users that stream and consume countless hours of live and recorded media. These services are often free to use but require you to have an account and generally hold your content behind advertisements. Some people don't need their videos to be available to the masses or just want more control over their content. Thankfully, with the power of open source software, anyone can set up a live streaming server.
* [Creating A Production Ready Multi Bitrate HLS VOD stream - Peer5 P2P Docs](https://docs.peer5.com/guides/production-ready-hls-vod/)  - Peer5 documentation
* [Creating a Master Playlist | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/creating_a_master_playlist#overview)  - 
* [FFmpeg and how to use it wrong](https://videoblerg.wordpress.com/2017/11/10/ffmpeg-and-how-to-use-it-wrong/)  - I’ve been in the streaming media industry since 2008 and have seen a lot of misinformation regarding both FFmpeg and libx264. In this post I hope to help shed some light on what does and does…
* [Guide to Mobile Video Streaming with HLS](https://mux.com/blog/mobile-hls-guide/)  - HTTP Live Streaming, also known as HLS, is the most common format used today for streaming video. If you're building a video streaming application today, you should probably use HLS. Apple created the HLS standard in 2009, and it is the required streaming format for iOS devices. Since then, Android
* [HLS Authoring Specification for Apple Devices | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/hls_authoring_specification_for_apple_devices)  - 
* [HLS adaptive streaming tutorial with CloudFront & JW Player | Miracle Tutorials](https://www.miracletutorials.com/hls-adaptive-streaming-tutorial-with-cloudfront-jw-player/)  - A step-by-step HLS adaptive streaming tutorial with CloudFront & JW Player in two parts. It is easier than you think. This tutorial presumes you have
* [HOW TO: View an HLS Stream in QuickTime or VLC – Softron Support Desk](https://softron.zendesk.com/hc/en-us/articles/207694617-HOW-TO-View-an-HLS-Stream-in-QuickTime-or-VLC?mobile_site=true)  - 
* [How To Setup Nginx For HLS Video Streaming On Centos 7](https://dev.to/samuyi/how-to-setup-nginx-for-hls-video-streaming-on-centos-7-3jb8)  - How to live stream videos with Nginx
* [How video streaming works on the web: An introduction](https://medium.com/canal-tech/how-video-streaming-works-on-the-web-an-introduction-7919739f7e1)  - Note: this article is an introduction to video streaming in JavaScript and is mostly targeted to web developers. A large part of the…
* [Internet Video Streaming — ABR part 1](https://medium.com/@eyevinntechnology/internet-video-streaming-abr-part-1-b10964849e19?source=userActivityShare-94bccb50d11-1559723768&_branch_match_id=664736558865703297)  - Background
* [Internet Video Streaming — ABR part 2](https://medium.com/@eyevinntechnology/internet-video-streaming-abr-part-2-dbce136b0d7c?source=userActivityShare-94bccb50d11-1559723862&_branch_match_id=664736952377004405)  - Background
* [Introduction to HTTP Live Streaming: HLS on Android and More](https://www.toptal.com/apple/introduction-to-http-live-streaming-hls)  - This article explains how HTTP Live Streaming works and demonstrates how to create an HLS player in Android.
* [Live Playlist (Sliding Window) Construction | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/live_playlist_sliding_window_construction)  - 
* [Live Video Transmuxing/Transcoding: FFmpeg vs TwitchTranscoder, Part 2](https://blog.twitch.tv/live-video-transmuxing-transcoding-ffmpeg-vs-twitchtranscoder-part-ii-4973f475f8a3?source=userActivityShare-94bccb50d11-1561003748&_branch_match_id=670105191114382351&gi=fd8d504494f4)  - 
* [Live Video Transmuxing/Transcoding: FFmpeg vs TwitchTranscoder, Part I](https://blog.twitch.tv/en/2017/10/10/live-video-transmuxing-transcoding-f-fmpeg-vs-twitch-transcoder-part-i-489c1c125f28/)  - 
* [Low Latency Live Streaming](https://docs.google.com/presentation/d/1ZwqWcweR5SqeMBRmJjSukWaHbpdPy-EPYvJCS23_n3U/edit?usp=sharing)  - Low Latency Live Streaming Apple LLHLS / CMAF Kevin Staunton-Lambert Solutions Architect R&D (July 2019) @kevleyski www.switch.tv
* [OTT Content Delivery](https://medium.com/@eyevinntechnology/ott-content-delivery-b43a35ef24f6)  - Background
* [OTT Content Delivery– Multi CDN](https://medium.com/@eyevinntechnology/ott-content-delivery-multi-cdn-8cd90ad2628a?source=userActivityShare-94bccb50d11-1560983307&_branch_match_id=670019455010399744)  - Background
* [Pyrmont Brewery](https://docs.google.com/presentation/d/15560aTv054w6bXKQ9gmBCE8gYwgtXhaPOHS1JcqTofk/edit?usp=sharing)  - Brewing in Pyrmont Prepared for The Pyrmont Historical Society, Nov 2019 Kev Staunton-Lambert pyrmontbrewery.com
* [Server-less Video Backend](https://medium.com/@eyevinntechnology/server-less-video-backend-1a142d1d2ba)  - In this blog post by Jonas Rydholm Birmé he describes how a completely server-less video backend on AWS would look like.
* [The structure of an MPEG-DASH MPD](https://www.brendanlong.com/the-structure-of-an-mpeg-dash-mpd.html)  - The MPEG-DASH Media Presentation Description (MPD) is an XML document containing information about media segments, their relationships and information necessary to choose between them, and other metadata that may be needed by clients. In this post, I describe the most important pieces of the MPD, starting from the top level (Periods) and going to the bottom (Segments).
* [Understanding the HTTP Live Streaming Architecture | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/understanding_the_http_live_streaming_architecture)  - 
* [VOD2Live](https://docs.google.com/presentation/d/1Ua76BBaZKtTmaZrlfM_eG0vwz0ZAqPIjreCSfB4qFQQ/edit?usp=sharing)  - VOD2Live Kevin Staunton-Lambert Solutions Architect R&D @kevleyski www.switch.tv
* [Video Encoding — Compression and Resolutions](https://medium.com/@eyevinntechnology/chessboard-for-beginners-video-encoding-compression-and-resolutions-bcefe04fa639)  - Written by: Boris Asadanin, Streaming Media Consultant at Eyevinn Technology
* [Video Tensorflow](https://docs.google.com/presentation/d/1NAqYWmFOwxJEacZCuPLdX0mRNRFPFgeRbsm22EaxerU/edit?usp=sharing)  - Using Tensorflow For Audience Measurement Kevin Staunton-Lambert Solutions Architect R&D @kevleyski www.switch.tv
* [Video on Demand Playlist Construction | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/video_on_demand_playlist_construction)  - 
* [WebAssembly (Wasm)](https://docs.google.com/presentation/d/1sonEk2neNVBcy8EzieUjWCNzj5SXN7dk-unkR_lpl8k/edit?usp=sharing)  - WebAssembly (Wasm) On the Edge Kevin Staunton-Lambert Solutions Architect R&D @kevleyski www.switch.tv Wasm)
* [WildFires](https://docs.google.com/presentation/d/1yiVEOq2rvtFynP1tLdJj7pBWkAEiE9g8BMaoryxRVrk/edit?usp=sharing)  - VOD2Live Kevin Staunton-Lambert Solutions Architect R&D @kevleyski Wild Fire! How video engineers can help save lives www.switch.tv
* [bash scripts to create VOD HLS stream with ffmpeg almighty (tested on Linux and OS X)](https://gist.github.com/mrbar42/ae111731906f958b396f30906004b3fa)  - bash scripts to create VOD HLS stream with ffmpeg almighty (tested on Linux and OS X) - README.md
* [matmoi/create-DASH-HLS](https://github.com/matmoi/create-DASH-HLS/)  - A tutorial to generate fMp4 files compatible with dash and HLS - matmoi/create-DASH-HLS
* [matmoi/create-DASH-HLS](https://github.com/matmoi/create-DASH-HLS)  - A tutorial to generate fMp4 files compatible with dash and HLS - matmoi/create-DASH-HLS

### Books
*Books on video streaming.*
[back to top](#readme) 

* [Communicating Pictures - 1st Edition](https://www.elsevier.com/books/communicating-pictures/bull/978-0-12-405906-1)  - Purchase Communicating Pictures - 1st Edition. Print Book & E-Book. ISBN 9780124059061, 9780080993744
* [Data Broadcasting: Understanding the ATSC Data Broadcast Standard](https://www.amazon.com/dp/0071375902/ref=cm_sw_r_oth_api_i_JHz-DbCZ4AJN3)  - 
* [Digital Television: MPEG-1, MPEG-2 and Principles of the DVB System](https://www.amazon.com/dp/0340691905/ref=cm_sw_r_oth_api_i_2Fz-DbHHGXNMZ)  - 
* [Digital Television: Technology and Standards ](https://www.amazon.com/dp/0470147830/ref=cm_sw_r_oth_api_i_wEz-DbZVSF65G])  - 
* [High Efficiency Video Coding (HEVC): Algorithms and Architectures (Integrated Circuits and Systems)](https://www.amazon.com/gp/product/3319068946/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)  - 
* [High Efficiency Video Coding: Coding Tools and Specification (Signals and Communication Technology)](https://www.amazon.com/gp/product/3662442752/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)  - 
* [Introduction to Digital Audio Coding and Standards](https://www.amazon.com/dp/1402073577/ref=cm_sw_r_oth_api_i_YIz-DbVR4VXKS)  - 
* [MPEG-4 Book](https://www.amazon.com/MPEG-4-Book-Fernando-Pereira/dp/0130616214/ref=sr_1_1?keywords=mpeg+4+book&qid=1576252504&s=books&sr=1-1)  - 
* [Producing Streaming Video for Multiple Screen Delivery](https://www.amazon.com/gp/product/0976259540/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)  - 
* [The MPEG Handbook, Second Edition ](https://www.amazon.com/dp/024080578X/ref=cm_sw_r_oth_api_i_oTz-Db86M94H9)  - 
* [Transporting Compressed Digital Video](https://www.amazon.com/dp/140207011X/ref=cm_sw_r_oth_api_i_DLz-DbTTZS7FP)  - 
* [Video Encoding by the Numbers: Eliminate the Guesswork from your Streaming Video](https://www.amazon.com/Video-Encoding-Numbers-Eliminate-Guesswork/dp/0998453005/ref=pd_bxgy_14_img_2/142-3989735-6086504?_encoding=UTF8&pd_rd_i=0998453005&pd_rd_r=6591968b-e54f-4fb1-8ab8-18e3f2a52f88&pd_rd_w=tWNbP&pd_rd_wg=RtRbb&pf_rd_p=09627863-9889-4290-b90a-5e9f86682449&pf_rd_r=JQP62Z6C5QJR49SEZNHP&psc=1&refRID=JQP62Z6C5QJR49SEZNHP)  - 

### Talks Presentations Podcasts
*Conference talks and pdf presentations and podcasts on streaming video .*
[back to top](#readme) 

* [Demuxed 2016](https://www.youtube.com/watch?v=kEo2TrXm7F4&list=PLkyaYNWEKcOekC2m9Na77G40Lmhb1bnsK)  - 2016 Demuxed talks & presentations
* [Demuxed 2017](https://www.youtube.com/watch?v=PSdhW-R9u6s&list=PLkyaYNWEKcOfntbMd6KtHhF7qpL9hj6of)  - 2017 Demuxed talks & presentations
* [Demuxed 2018](https://www.youtube.com/watch?v=bfK_f7GBA8s&list=PLkyaYNWEKcOfARqEht42i1P4kBemzEV2V)  - 2018  Demuxed talks & presentations
* [Demuxed 2019](https://m.youtube.com/playlist?list=PLkyaYNWEKcOf_C_6W45abNvXMb40xUUqh)  - 2019 Demuxed talks & presentations
* [Demuxed | Heavybit](https://www.heavybit.com/library/podcasts/demuxed)  - Demuxed is a podcast made for and by engineers working with video. Brought to you by Heavybit.
* [From Sys Admin to Netflix SRE](https://www.youtube.com/watch?v=lZI51YzIgVE)  - Talk by Jonah Horowitz, Albert Tobey What does it take to be a Netflix SRE? With tens of thousands of Linux instances in a distributed system architecture, a...
* [Mile High Video 2018 Proceedings](http://mile-high.video/files/mhv2018)  - Mile High Video 2018 talks & presentations
* [Mile High Video 2019 Proceedings](http://mile-high.video/files/mhv2019)  - Mile High Video 2019 talks & presentations
* [The Video Insiders](https://thevideoinsiders.simplecast.com/episodes)  - Video Insiders Podcast

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
* [tjenkinson/mock-hls-server](https://github.com/tjenkinson/mock-hls-server)  - Fake a live/event HLS stream from a VOD one. Useful for testing. - tjenkinson/mock-hls-server
* [videojs/m3u8-parser](https://github.com/videojs/m3u8-parser)  - An m3u8 parser.
* [yuhuili-lab/Tide](https://github.com/yuhuili-lab/Tide)  - Simple m3u8 and MPEG-DASH MPD video downloader using libcurl - yuhuili-lab/Tide
* [zhaiweiwei/nginx-hls](https://github.com/zhaiweiwei/nginx-hls)  - Contribute to zhaiweiwei/nginx-hls development by creating an account on GitHub.

## DASH
*DASH tools, libraries, and resources.*

* [Dash-Industry-Forum/DASH-IF-Conformance](https://github.com/Dash-Industry-Forum/DASH-IF-Conformance)  - This repository provides the source code for MPEG-DASH/DASH-IF Conformance Software/Validator. It has been extended according to further standards, such as CMAF, DVB-DASH, HbbTV, and CTA WAVE. - Da...
* [Dash-Industry-Forum/ISOSegmentValidator](https://github.com/Dash-Industry-Forum/ISOSegmentValidator)  - Contribute to Dash-Industry-Forum/ISOSegmentValidator development by creating an account on GitHub.
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
* [djvergad/dash](https://github.com/djvergad/dash)  - An MPEG/DASH client-server module for simulating rate adaptation mechanisms over HTTP/TCP. - djvergad/dash
* [mahbubcseju/MPEG-DASH-Downloader](https://github.com/mahbubcseju/MPEG-DASH-Downloader)  - Contribute to mahbubcseju/MPEG-DASH-Downloader development by creating an account on GitHub.
* [mp4dash | Bento4](https://www.bento4.com/documentation/mp4dash/)  - 
* [nickdesaulniers/combine-mpd](https://github.com/nickdesaulniers/combine-mpd)  - Combine MPEG DASH MPD manifest files.
* [sangwonl/python-mpegdash](https://github.com/caststack/python-mpegdash)  - MPEG-DASH MPD(Media Presentation Description) Parser - sangwonl/python-mpegdash
* [stultus/mp4-to-mpegdash-py](https://github.com/stultus/mp4-to-mpegdash-py)  - Python Script to convert a MP4 file into onDemand MPEG-DASH - stultus/mp4-to-mpegdash-py
* [tchakabam/dash-proxy](https://github.com/tchakabam/dash-proxy)  - Experimental MPEG-DASH media gateway - proxy on-the-fly modified MP4 segment metadata - tchakabam/dash-proxy
* [theolampert/dash-server](https://github.com/theolampert/dash-server)  - Small, command-line HTTP/2 file server for serving MPEG-DASH content. - theolampert/dash-server
* [videojs/mpd-parser](https://github.com/videojs/mpd-parser)  - Contribute to videojs/mpd-parser development by creating an account on GitHub.
* [videojs/videojs-contrib-dash](https://github.com/videojs/videojs-contrib-dash)  - Video.js plugin for supporting the MPEG-DASH playback through a video.js player - videojs/videojs-contrib-dash

## Encoding
*Encoding tools, libraries, and resources.*

* [A Large-Scale Comparison of x264, x265, and libvpx](https://medium.com/netflix-techblog/a-large-scale-comparison-of-x264-x265-and-libvpx-a-sneak-peek-2e81e88f8b0f)  - a Sneak Peek
* [Bento4 | Fast, Modern Tools and C++ Class Library for all your MP4 and DASH media format needs](https://www.bento4.com/)  - 
* [Introducing SVT-AV1: a scalable open-source AV1 framework](https://medium.com/netflix-techblog/introducing-svt-av1-a-scalable-open-source-av1-framework-c726cce3103a)  - by Andrey Norkin, Joel Sole, Kyle Swanson, Mariana Afonso, Anush Moorthy, Anne Aaron
* [Snowmix - The Swiss Army Knife of Open Source Live Video Mixing.](https://snowmix.sourceforge.io)  - Snowmix Video Mixer
* [Zulko/moviepy](https://github.com/Zulko/moviepy)  - 
* [alfg/docker-bento4](https://github.com/alfg/docker-bento4)  - A dockerized Bento4 from source. Built on Alpine Linux.  - alfg/docker-bento4
* [avTranscoder/avTranscoder](https://github.com/avTranscoder/avTranscoder)  - C++ API for LibAV / FFMpeg.d
* [bbc/brave](https://github.com/bbc/brave)  - Basic Real-time AV Editor - allowing you to preview, mix, and route live audio and video streams on the cloud - bbc/brave
* [bfansports/CloudTranscode](https://github.com/bfansports/CloudTranscode)  - Distributed videos and images encoding/transcoding using Amazon SFN, FFMpeg and ImageMagic - bfansports/CloudTranscode
* [bloc97/Anime4K](https://github.com/bloc97/Anime4K)  - A High-Quality Real Time Upscaler for Anime Video.
* [cannonbeach/ott-packager](https://github.com/cannonbeach/ott-packager)  - OTT/ABR streaming encoder (H264/HEVC) and packager for DASH and HLS - cannonbeach/ott-packager
* [escaped/django-video-encoding](https://github.com/escaped/django-video-encoding)  - django-video-encoding helps to convert your videos into different formats and resolutions. - escaped/django-video-encoding
* [jliljebl/flowblade](https://github.com/jliljebl/flowblade)  - 
* [mltframework/mlt](https://github.com/mltframework/mlt)  - MLT Multimedia Framework.
* [olaris / olaris-server](https://gitlab.com/olaris/olaris-server)  - GitLab.com
* [ptrandev/swift-encoder](https://github.com/ptrandev/swift-encoder)  - A fire-and-forget shell script that encodes multiple video and audio files with ffmpeg. - ptrandev/swift-encoder
* [realeyes-media/demo-encoder](https://github.com/realeyes-media/demo-encoder/)  - A nodejs encoding system based on ffmpeg and configured to write HLS streaming files to S3 - realeyes-media/demo-encoder
* [realeyes-media/demo-encoder](https://github.com/realeyes-media/demo-encoder)  - A nodejs encoding system based on ffmpeg and configured to write HLS streaming files to S3 - realeyes-media/demo-encoder
* [senko/avtk](https://github.com/senko/avtk)  - 
* [sitkevij/mp](https://github.com/sitkevij/mpi)  - 
* [snickers/snickers](https://github.com/snickers/snickers)  - :chocolate_bar: An open source alternative to the video cloud encoding services. - snickers/snickers
* [voc/voctomix](https://github.com/voc/voctomix)  - Full-HD Software Live-Video-Mixer in python.

### AV1
*AV1 libraries, tools, examples, and resources.*
[back to top](#readme) 

* [AV1 Codec](https://docs.google.com/presentation/d/12_Vewc0SDpB1FycflfT4us9eipRCy0HWJVSaDMDifRs/edit?usp=sharing)  - Working with the AV1 Codec Kevin Staunton-Lambert Solutions Architect R&D @kevleyski www.switch.tv
* [Eyevinn/av1-player](https://github.com/Eyevinn/av1-player)  - Eyevinn AV1 player.

### HEVC
*HEVC (h265) libraries, tools, examples, and resources.*
[back to top](#readme) 

* [ Suggestion for x265's --tune film - Doom9's Forum](https://forum.doom9.org/showthread.php?t=172458)  -  Suggestion for x265's --tune film High Efficiency Video Coding (HEVC)
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
* [Video Quality Evaluation Methodology and Verification Testing of HEVC Compression Performance](https://ieeexplore.ieee.org/ielx7/76/7372356/07254155.pdf?tp=&arnumber=7254155&isnumber=7372356&ref=)  - 
* [multicoreware / x265 / wiki / Home — Bitbucket](https://bitbucket.org/multicoreware/x265/wiki/Home)  - 
* [x265 Documentation — x265  documentation](https://x265.readthedocs.io/en/default/)  - 

### VP9
*VP9 libraries, tools, examples, and resources.*
[back to top](#readme) 


## Streaming Server and Storage
*Packagers, origins (s3, gcs), and data movement for linear and finite playback. *

* [ant-media/Ant-Media-Server](https://github.com/ant-media/Ant-Media-Server)  - Ant Media Server supports RTMP, RTSP, WebRTC and Adaptive Bitrate. It can also record videos in MP4, HLS and FLV - ant-media/Ant-Media-Server
* [haiwen/seafile](https://github.com/haiwen/seafile)  - High performance file syncing and sharing, with also Markdown WYSIWYG editing, Wiki, file label and other knowledge management features. - haiwen/seafile
* [openstack/swift](https://github.com/openstack/swift)  - OpenStack Storage (Swift).
* [ossrs/srs](https://github.com/ossrs/srs)  - SRS is a simple live streaming cluster, a simple joy. - ossrs/srs
* [rclone/rclone](https://github.com/rclone/rclone)  - rsync for cloud storage - Google Drive, Amazon Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Cloudfiles, Google Cloud Storage, Yandex Files - rclone/rclone

## Reading
*A list of reading articles, blogs, and newsletters for video streaming.*

* [9 Best Home Server Apps to Automate Media Management](https://www.smarthomebeginner.com/best-home-server-apps/)  - These are top 9 best home server apps to automate media management, so you get the latest Movies, Music and TV Shows in the best quality available.
* [Demystifying HTML5 Video Player](https://medium.com/@eyevinntechnology/demystifying-html5-video-player-e480846328f0)  - In this post we will go under the hood of a HTML video player for video streaming. With the exception of Apple and their browser Safari, no…
* [Extracting contextual information from video assets](https://medium.com/netflix-techblog/extracting-contextual-information-from-video-assets-ee9da25b6008)  - for an improved Netflix user experience
* [IMF: A Prescription for Versionitis](https://medium.com/netflix-techblog/imf-a-prescription-for-versionitis-e0b4c1865c20)  - the emerging Interoperable Master Format standard
* [Inside MPEG's Ambitious Plan to Launch 3 Video Codecs in 2020](https://www.streamingmedia.com/Articles/Editorial/Featured-Articles/Inside-MPEGs-Ambitious-Plan-to-Launch-3-Video-Codecs-in-2020-134694.aspx)  - The pace of innovation is getting faster and the demands on video codecs are getting greater. MPEG's three-part plan answers questions of royalties, licensing, and computational efficiency. Meet VVC, MPEG-5 Part 1 (EVC), and MPEG-5 Part 2 (LCEVC).
* [Quantifying packaging overhead](https://mux.com/blog/quantifying-packaging-overhead-2)  - Mux makes adding video to your app or website as easy as making a single API call. But behind the scenes is a large multistep process to analyze and transform the video into something that can be easily consumed by a device. This process is commonly called a media “pipeline”
* [Server-less Just-in-Time Packaging with AWS Fargate and Unified Origin by Unified Streaming](https://medium.com/@eyevinntechnology/server-less-just-in-time-packaging-with-aws-fargate-and-unified-origin-by-unified-streaming-c1682dc051ca?source=userActivityShare-94bccb50d11-1559724204&_branch_match_id=664738392430917730)  - In this blog article Jonas Rydholm Birmé describes how he created a server-less just-in-time packaging origin, using AWS ECS Fargate tasks…
* [Server-less Just-in-Time Packaging with AWS Fargate and Unified Origin by Unified Streaming](https://medium.com/@eyevinntechnology/server-less-just-in-time-packaging-with-aws-fargate-and-unified-origin-by-unified-streaming-c1682dc051ca?source=userActivityShare-94bccb50d11-1560983627&_branch_match_id=670020794794030328)  - In this blog article Jonas Rydholm Birmé describes how he created a server-less just-in-time packaging origin, using AWS ECS Fargate tasks…
* [Streaming Live From the Battlefield: Military Video in 2019](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=135141)  - Metadata and low-latency video create a tactical advantage in intelligence-gathering and decision making. Discover why HEVC is gaining momentum in the armed forces, and Android is preferred over iOS.
* [The Netflix IMF Workflow](https://medium.com/netflix-techblog/the-netflix-imf-workflow-f45dd72ed700?source=userActivityShare-94bccb50d11-1568773157&_branch_match_id=702692448596112473)  - interesting architectural implications
* [VOD on AWS](https://s3.amazonaws.com/solutions-reference/video-on-demand-on-aws/latest/video-on-demand-on-aws.pdf)  - 
* [Video Coding - BBC R&D](https://www.bbc.co.uk/rd/projects/video-coding)  - BBC video encoding R&D home page
* [Video in the War Zone: The Current State of Military Streaming](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=101310)  - For the armed forces, streaming is a matter of national security. Here's an exclusive look at how the military, from analysts to ground troops, is using streaming video.

## Specs and Standards
*Latest offical specs and standards related to video streaming.*

* [DASH-IF IOPs](https://dashif.org/guidelines/)  - 
* [How Do I Become an ANSI Member](https://www.ansi.org/membership/how_to_join/how_3)  - 
* [latest HLS Spec](https://tools.ietf.org/html/draft-pantos-hls-rfc8216bis-05)  - 

### MPEG
*MPEG meetings, standards, and resources. *
[back to top](#readme) 

* [MPEG About](https://mpeg.chiariglione.org/about)  - 
* [MPEG Meetings](https://mpeg.chiariglione.org/meetings)  - 
* [MPEG future](http://mpegfuture.org/)  - 

## Players
*Client players, libraries, tools, and examples.*

* [IvanoBilenchi/Adaptive-Video-Player](https://github.com/IvanoBilenchi/Adaptive-Video-Player)  - HLS player for iOS that supports manual selection for the quality of adaptive streams - IvanoBilenchi/Adaptive-Video-Player
* [davidAgo4g/VideoPlayer-iOS](https://github.com/davidAgo4g/VideoPlayer-iOS)  - A library based on FFMPEG to play video files on iOS using OpenGLES and AudioQueue. Build with theos - davidAgo4g/VideoPlayer-iOS
* [imoreapps/ffmpeg-avplayer-for-ios-tvos](https://github.com/imoreapps/ffmpeg-avplayer-for-ios-tvos)  - A tiny but powerful iOS and Apple TV OS av player framework that's based on the FFmpeg library. - imoreapps/ffmpeg-avplayer-for-ios-tvos
* [lightspark/lightspark](https://github.com/lightspark/lightspark)  - An open source flash player implementation.
* [matvp91/indigo-player](https://github.com/matvp91/indigo-player)  - Highly extensible, modern, JavaScript video player. Handles MPEG-Dash / HLS / MPEG-4 and is built on top of the HTML5 video element. - matvp91/indigo-player
* [mpv-player/mpv](https://github.com/mpv-player/mpv)  - 🎥 Command line video player.
* [nytimes/ios-360-videos](https://github.com/nytimes/ios-360-videos)  - NYT360Video plays 360-degree video streamed from an AVPlayer on iOS. - nytimes/ios-360-videos
* [peak3d/inputstream.adaptive](https://github.com/peak3d/inputstream.adaptive)  - kodi inputstream addon for several manifest types.
* [ruffle-rs/ruffle](https://github.com/ruffle-rs/ruffle)  - A Flash Player emulator written in Rust.
* [tjenkinson/media-element-syncer](https://github.com/tjenkinson/media-element-syncer)  - Synchronise two or more HTML5 media elements.
* [ustwo/videoplayback-ios](https://github.com/ustwo/videoplayback-ios)  - Swift AVPlayer wrapper using the VIPER architecture. Currently a work in progress  - ustwo/videoplayback-ios
* [videolan/vlc](https://github.com/videolan/vlc)  - VLC media player - All pull requests are ignored, please follow https://wiki.videolan.org/Sending_Patches_VLC/ - videolan/vlc
* [vitalets/awesome-smart-tv](https://github.com/vitalets/awesome-smart-tv)  - :zap:A curated list of awesome resources for building Smart TV apps - vitalets/awesome-smart-tv

### Android
*Android and fireTV tools, sdks, and examples.*
[back to top](#readme) 

* [google/ExoPlayer](https://github.com/google/ExoPlayer)  - ExoPlayer is an application level media player for Android.

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
* [StyleShare/HLSCachingReverseProxyServer](https://github.com/StyleShare/HLSCachingReverseProxyServer)  - A simple local reverse proxy server for HLS segment cache - StyleShare/HLSCachingReverseProxyServer
* [VeinGuo/VGPlayer](https://github.com/VeinGuo/VGPlayer)  - 📺  A simple iOS video player by Vein.
* [googleads/google-media-framework-ios](https://github.com/googleads/google-media-framework-ios)  - The Google Media Framework (GMF) is a lightweight media player designed to make video playback and integration with the Google IMA SDK on iOS easier. - googleads/google-media-framework-ios
* [hanton/HTY360Player](https://github.com/hanton/HTY360Player)  - Open Source iOS 360 Degree Panorama Video Player.
* [iina/iina](https://github.com/iina/iina)  - The modern video player for macOS.
* [kodlian/TVVLCPlayer](https://github.com/kodlian/TVVLCPlayer)  - TVVLCPlayer lets you integrate easily a powerfull video player with playback control views to your tvOS apps. - kodlian/TVVLCPlayer
* [libobjc/SGPlayer](https://github.com/libobjc/SGPlayer)  - A powerful media play framework for iOS, macOS, and tvOS. - libobjc/SGPlayer
* [masterjk/ios-avplayer-http-capture](https://github.com/masterjk/ios-avplayer-http-capture)  - iOS based application that embeds the AVPlayer and capture HTTP headers and send it back to the iOS application.  It internally embeds a proxy server. - masterjk/ios-avplayer-http-capture
* [noreasonprojects/ModernAVPlayer](https://github.com/noreasonprojects/ModernAVPlayer)  - ModernAVPlayer is a persistence AVPlayer wrapper. 
* [piemonte/Player](https://github.com/piemonte/Player)  - ▶️ video player in Swift, simple way to play and stream media on iOS/tvOS - piemonte/Player
* [renzifeng/ZFPlayer](https://github.com/renzifeng/ZFPlayer)  - Support customization of any player SDK and control layer
* [tanersener/mobile-ffmpeg](https://github.com/tanersener/mobile-ffmpeg)  - FFmpeg for Android, iOS and tvOS.
* [vitoziv/VIMediaCache](https://github.com/vitoziv/VIMediaCache)  - Cache media file while play media using AVPlayer.
* [xiewei-wayne/FFEngine.framework](https://github.com/xiewei-wayne/FFEngine.framework)  - FFEngine framework is a high performance player sdk for iOS based on ffmpeg. - xiewei-wayne/FFEngine.framework
* [xiewei-wayne/rtmp-video-player-for-ios](https://github.com/xiewei-wayne/rtmp-video-player-for-ios)  - Based on FFEngine framework, a rtmp video player for apple iOS devices. - xiewei-wayne/rtmp-video-player-for-ios

### Roku
*Roku app tools, libraries,and examples.*
[back to top](#readme) 

* [Audio and Video Support](https://developer.roku.com/docs/specs/streaming.md#AudioandVideoSupport-AdaptiveBitrateFormats)  - Roku provides the simplest way to stream entertainment to your TV. On your terms. With thousands of available channels to choose from.
* [CCecilia/roku-suite-desktop](https://github.com/CCecilia/roku-suite-desktop)  - Tool suite for Roku channel development.
* [MediaBrowser/Emby.Roku](https://github.com/MediaBrowser/Emby.Roku)  - Emby for Roku. 
* [Playing Video Examples](https://developer.roku.com/docs/developer-program/core-concepts/playing-videos.md#PlayingVideos-Examples)  - Roku provides the simplest way to stream entertainment to your TV. On your terms. With thousands of available channels to choose from.
* [Roku](https://developer.roku.com/docs/specs/streaming.md)  - Roku provides the simplest way to stream entertainment to your TV. On your terms. With thousands of available channels to choose from.
* [T-Pham/RokuJSONHelperNode](https://github.com/T-Pham/RokuJSONHelperNode)  - Roku SceneGraph JSON Helper.
* [Video Node Docs](https://developer.roku.com/docs/references/scenegraph/media-playback-nodes/video.md)  - Roku provides the simplest way to stream entertainment to your TV. On your terms. With thousands of available channels to choose from.
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
* [Eyevinn/abr-player-chrome](https://github.com/Eyevinn/abr-player-chrome)  - Chrome extension that uses Eyevinn HTML player to be able to play HLS and MPEG-DASH natively - Eyevinn/abr-player-chrome
* [Eyevinn/channel-engine-multiview](https://github.com/Eyevinn/channel-engine-multiview)  - A multiview frontend for Eyevinn Channel Engine.
* [Eyevinn/docker-html5player](https://github.com/Eyevinn/docker-html5player)  - A Docker containerized HTML5 player based on Shaka Player - Eyevinn/docker-html5player
* [Eyevinn/eyevinn-player](https://github.com/Eyevinn/eyevinn-player)  - Throttled video player to test video streams.
* [Eyevinn/ott-multiview](https://github.com/Eyevinn/ott-multiview)  - This is a web based multiview screen for HLS and MPEG-DASH streams based on hls.js and Shaka Player. - Eyevinn/ott-multiview
* [MoePlayer/DPlayer](https://github.com/MoePlayer/DPlayer)  - :lollipop: Wow, such a lovely HTML5 danmaku video player - MoePlayer/DPlayer
* [bbc/bigscreen-player](https://github.com/bbc/bigscreen-player)  - Simplified media playback for bigscreen devices.
* [bytedance/xgplayer](https://github.com/bytedance/xgplayer)  - A HTML5 video player with a parser that saves traffic - bytedance/xgplayer
* [epiclabs-io/epic-video-comparator](https://github.com/epiclabs-io/epic-video-comparator)  - Javascript library which implements a video comparator component: two overlaped and synchronized video players each one playing an independent source. - epiclabs-io/epic-video-comparator
* [sampotts/plyr](https://github.com/sampotts/plyr)  - A simple HTML5, YouTube and Vimeo player.
* [video-dev/hls.js](https://github.com/video-dev/hls.js)  - JavaScript HLS client using Media Source Extension - video-dev/hls.js
* [videojs/http-streaming](https://github.com/videojs/http-streaming)  - HLS, DASH, and future HTTP streaming protocols library for video.js - videojs/http-streaming
* [videojs/video.js](https://github.com/videojs/video.js)  - Video.js - open source HTML5 & Flash video player.
* [vimond/replay](https://github.com/vimond/replay)  - A React video player facilitating adaptive stream playback with custom UI and a React-friendly API. - vimond/replay

## FFMPEG
*FFMPEG libraries, configs, tools, and examples.*

* [Ch00k/ffmpy](https://github.com/Ch00k/ffmpy)  - 
* [ElderByte-/docker-java-media](https://github.com/ElderByte-/docker-java-media)  - JRE 10 (Java 10) and media tools (ffmpeg).
* [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)  - Mirror of git://source.ffmpeg.org/ffmpeg.git.
* [FallingSnow/h265ize](https://github.com/FallingSnow/h265ize)  - A node utility utilizing ffmpeg to encode videos with the hevc codec. - FallingSnow/h265ize
* [Generate MPEG-TS from file with ffmpeg](https://medium.com/@eyevinntechnology/generate-mpeg-ts-from-file-with-ffmpeg-7561181e6369?source=userActivityShare-94bccb50d11-1560983471&_branch_match_id=670020142756633081)  - In this post I will describe how an MPEG-TS multicast stream can be generated with ffmpeg by looping an MP4 file and a Docker container…
* [How to generate a fmp4 hls live stream with FFMPEG](https://nomadyun.wordpress.com/2018/04/12/how-to-generate-a-fmp4-hls-live-stream-with-ffmpeg/)  - ffmpeg -re -stream_loop -1 -i voweb.mp4 -hls_fmp4_init_filename init.mp4 -vf “settb=AVTB,setpts=’trunc(PTS/1K)*1K+st\(1,trunc(RTCTIME/1K))-1K*trunc(ld(1)/1K)’,\ drawtext=fontfile=…
* [Is it possible to get FFmpeg to use hardware acceleration for HEVC transcoding on macOS?](https://superuser.com/questions/1295957/ffmpeg-and-hardware-acceleration-of-hevc-transcoding-on-mac)  - I have a MacBook Pro with a Kaby Lake processor running macOS High Sierra (10.12). Is it possibe somehow to setup FFmpeg to utilize hardware encoding of HEVC with toolbox, instead of libx265?
* [Kagami/ffmpeg.js](https://github.com/Kagami/ffmpeg.js)  - Port of FFmpeg with Emscripten.
* [Loop file and generate multiple video bitrates muxed in MPEG-TS with ffmpeg](https://medium.com/@eyevinntechnology/loop-file-and-generate-multiple-video-bitrates-muxed-in-mpeg-ts-with-ffmpeg-85658d0b74bb?source=userActivityShare-94bccb50d11-1560983383&_branch_match_id=670019768959110835)  - In a previous post I described how an MPEG-TS multicast stream can be generated with ffmpeg by looping an MP4 file. In this post I will…
* [WritingMinds/ffmpeg-android-java](https://github.com/WritingMinds/ffmpeg-android-java)  - Android java library for FFmpeg binary compiled using https://github.com/writingminds/ffmpeg-android - WritingMinds/ffmpeg-android-java
* [bcoudurier/FFmbc](https://github.com/bcoudurier/FFmbc)  - FFmpeg customized for broadcast and professional usage - bcoudurier/FFmbc
* [binoculars/aws-lambda-ffmpeg](https://github.com/binoculars/aws-lambda-ffmpeg)  - An S3-triggered Amazon Web Services Lambda function that runs your choice of FFmpeg 🎬 commands on a file  🎥 and uploads the outputs to a bucket. - binoculars/aws-lambda-ffmpeg
* [bramp/ffmpeg-cli-wrapper](https://github.com/bramp/ffmpeg-cli-wrapper)  - Java wrapper around the FFmpeg command line tool.
* [compile and install latest ffmpeg source as pkg](https://gist.github.com/krzemienski/e51a0b7a6ba77e616f954e516783270c#file-compile-and-install-latest-ffmpeg-source-sh-L2)  - compile and install latest ffmpeg source as pkg. GitHub Gist: instantly share code, notes, and snippets.
* [cuda/ubuntu16.04/ffmpeg-gpu/Dockerfile · master · nvidia / container-images / samples](https://gitlab.com/nvidia/container-images/samples/blob/master/cuda/ubuntu16.04/ffmpeg-gpu/Dockerfile)  - Sample Dockerfiles for Docker Hub images
* [gitfu/manifesto](https://github.com/gitfu/manifesto)  - Manifesto is an HLS tool for creating multiple variants, a master.m3u8 file, and converting 608 captions to segmented webvtt subtitles via ffmpeg. - gitfu/manifesto
* [jrottenberg/ffmpeg](https://github.com/jrottenberg/ffmpeg)  - Docker build for FFmpeg on Ubuntu / Alpine / Centos 7 / Scratch - jrottenberg/ffmpeg
* [kewlbear/FFmpeg-iOS-build-script](https://github.com/kewlbear/FFmpeg-iOS-build-script)  - Shell scripts to build FFmpeg for iOS and tvOS. 
* [kkroening/ffmpeg-python](https://github.com/kkroening/ffmpeg-python)  - 
* [kokorin/Jaffree](https://github.com/kokorin/Jaffree)  - Java ffmpeg and ffprobe command-line wrapper.
* [markus-perl/ffmpeg-build-script](https://github.com/markus-perl/ffmpeg-build-script)  - The FFmpeg build script provides an easy way to build a static FFmpeg on OSX and Linux with non-free codecs included. - markus-perl/ffmpeg-build-script
* [microshow/RxFFmpeg](https://github.com/microshow/RxFFmpeg)  - 🔥RxFFmpeg 是基于 ( FFmpeg 4.0 + X264 + mp3lame + fdk-aac )
* [nextbreakpoint/ffmpeg4java](https://github.com/nextbreakpoint/ffmpeg4java)  - FFmpeg4Java provides a JNI wrapper of FFmpeg library - nextbreakpoint/ffmpeg4java
* [silencecorner/jre-ffmpeg-apline](https://github.com/silencecorner/jre-ffmpeg-apline)  - Dockerfile [jre8](https://github.com/fabric8io-images/java) and [ffmpeg](https://hub.docker.com/r/jrottenberg/ffmpeg)  - silencecorner/jre-ffmpeg-apline
* [slhck/ffmpeg-encoding-course](https://github.com/slhck/ffmpeg-encoding-course)  - An introduction to FFmpeg and its tools. 
* [transitive-bullshit/awesome-ffmpeg](https://github.com/transitive-bullshit/awesome-ffmpeg)  - 👻 A curated list of awesome FFmpeg resources.
* [unosquare/ffmediaelement](https://github.com/unosquare/ffmediaelement)  - FFME: The Advanced WPF MediaElement (based on FFmpeg) - unosquare/ffmediaelement
* [x264 FFmpeg Options Guide - Linux Encoding](https://sites.google.com/site/linuxencoding/x264-ffmpeg-mapping)  - 

## Audio
*Audio libraries, tools, and examples.*

* [Adjust and Normalize Your Music Files with FFMPEG - Make Tech Easier](https://www.maketecheasier.com/normalize-music-files-with-ffmpeg/)  - If your music files are too loud, too soft, or have obnoxious peaks and irregular volume, you can use FFmpeg to normalize your music files. Here's how.
* [Audio Loudness  |  Conversational Actions  |  Google Developers](https://developers.google.com/assistant/tools/audio-loudness)  - 
* [Audio normalization with ffmpeg using loudnorm (ebur128) filter](https://bytesandbones.wordpress.com/2017/03/16/audio-nomalization-with-ffmpeg-using-loudnorm-ebur128-filter/)  - 
* [EBU Evaluations of Multichannel Audio Codecs](https://tech.ebu.ch/docs/tech/tech3324.pdf)  - 
* [EBU R128 Introduction - Florian Camerer](https://www.youtube.com/watch?v=iuEtQqC-Sqo)  - Florian Camerer gives an introduction to the European Broadcasting Union's R128 Broadcast Standard and speaks in general about perceived loudness, peak norma...
* [How to Set Audio Levels for Video](https://www.premiumbeat.com/blog/how-to-set-audio-levels-for-video/)  - Bad sound can easily ruin good footage. Use these tips when it comes time to set audio levels for video and film projects.
* [Loudness Explained Page | Music Tribe - TC Electronic](https://www.tcelectronic.com/brand/tcelectronic/loudness-explained#googtrans(en|en))  - tcelectronic, 
* [Quick Tutorial: How to Increase Volume in Audacity [2019 Update]](https://www.iskysoft.com/video-editing/how-to-increase-volume-in-audacity.html)  - How to increase volume in Audacity? This article will guide you to change volume in Audacity and its alternative tool. You can pick up one of them to edit volume in Audacity as you like.
* [ReplayGain - Audacity Forum](https://forum.audacityteam.org/viewtopic.php?t=63067)  - 
* [Techniques for Establishing and Maintaining Audio Loudness for Digital Television](https://www.atsc.org/wp-content/uploads/2015/03/Techniques-for-establishing-and-maintaining-audio-loudness.pdf)  - 
* [hybrik/hybrik-samples](https://github.com/hybrik/hybrik-samples/blob/master/Feature%20Examples/Filters/ebu_r128_audio_normalization.json)  - Hybrik Samples.
* [normalizing Audio](https://www.learndigitalaudio.com/normalize-audio)  - 
* [slhck/ffmpeg-normalize](https://github.com/slhck/ffmpeg-normalize#examples)  - Audio Normalization for Python/ffmpeg.
* [superpoweredSDK/Low-Latency-Android-iOS-Linux-Windows-tvOS-macOS-Interactive-Audio-Platform](https://github.com/superpoweredSDK/Low-Latency-Android-iOS-Linux-Windows-tvOS-macOS-Interactive-Audio-Platform)  - 🇸Superpowered Audio, Networking and Cryptographics SDKs. High performance and cross platform on Android, iOS, macOS, tvOS, Linux, Windows and modern web browsers. - superpoweredSDK/Low-Latency-Andr...

## Subtitles and Captions
*Subtitling & Closed Caption libraries, tools, and examples.*

* [BingLingGroup/autosub](https://github.com/BingLingGroup/autosub)  - Command-line utility to transcribe/translate from video/audio/subtitles to subtitles  - BingLingGroup/autosub
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
* [IMSC Specification](https://www.w3.org/TR/ttml-imsc1.1/)  - 
* [IMSC renderer](https://sandflow.com/imsc1proc/index.html)  - 
* [IMSC validator](https://apps.sandflow.com/imscV/)  - 
* [IRT/BaseX IMSC validator](https://subcheck.io/#/)  - 
* [The ultimate guide to CCs](https://www.3playmedia.com/resources/popular-topics/closed-captioning/)  - 
* [Web Video Text Tracks Format (WebVTT)](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)  - Web Video Text Tracks Format (WebVTT) is a format for displaying timed text tracks (such as subtitles or captions) using the track element.
* [abinashmeher999/voice-data-extract](https://github.com/abinashmeher999/voice-data-extract)  - A command line interface to combine text information from subtitles with voice data in the video. Provides a convenient way to generate training data for speech-recognition purposes. - abinashmeher...
* [active-video/subtitles](https://github.com/active-video/subtitles)  - AV Platform MPEG DASH subtitles.
* [apm1467/videocr](https://github.com/apm1467/videocr)  - Extract hardcoded subtitles from videos using machine learning - apm1467/videocr
* [awslabs/serverless-subtitles](https://github.com/awslabs/serverless-subtitles)  - Serverless Subtitles can handle a video input, extract the sound, transcript it and generate different subtitle files for your video. - awslabs/serverless-subtitles
* [cessen/subs_extract](https://github.com/cessen/subs_extract)  - Extracts per-sentence subtitles + audio from a subtitle file + video file. - cessen/subs_extract
* [djstava/manifesto](https://github.com/djstava/manifesto)  - HLS multibitrate encoding with WebVTT subtitles and master.m3u8 generator in one easy step.
* [federicocalendino/pysub-parser](https://github.com/federicocalendino/pysub-parser)  - Utility to extract the text and timestamps of a subtitle file (.srt, .ssa, .sub, .txt). - federicocalendino/pysub-parser
* [glut23/webvtt-py](https://github.com/glut23/webvtt-py)  - Read, write and segment WebVTT caption files in Python.
* [jnorton001/pycaption-cli](https://github.com/jnorton001/pycaption-cli)  - A command line interface for the pycaption module. - jnorton001/pycaption-cli
* [opencoconut/webvtt-ruby](https://github.com/opencoconut/webvtt-ruby)  - WebVTT Ruby parser and segmenter.
* [osk/node-webvtt](https://github.com/osk/node-webvtt)  - Parse WebVTT files, segments and generates HLS playlists for them.
* [sandflow/imscJS](https://github.com/sandflow/imscJS/)  - 
* [shawnsky/extract-subtitles](https://github.com/shawnsky/extract-subtitles)  - Extract Subtitles From Video
* [smacke/subsync](https://github.com/smacke/subsync)  - Automagically synchronize subtitles with video.
* [statsbiblioteket/tv-subtitle-extraction](https://github.com/statsbiblioteket/tv-subtitle-extraction)  - System for extraction of subtitles from TV broadcasts. - statsbiblioteket/tv-subtitle-extraction
* [wargarblgarbl/libgosubs](https://github.com/wargarblgarbl/libgosubs)  - 
* [xinnjie/extract-subtitle](https://github.com/xinnjie/extract-subtitle)  - extract subtitles from video.

## Ads
*Ads in streaming video related libraries, tools, examples, and resources.*

* [Eyevinn/adxchange-engine](https://github.com/Eyevinn/adxchange-engine)  - Eyevinn Adxchange Engine is a microservice placed between the server-side ad-insertion component and the adserver or SSP - Eyevinn/adxchange-engine
* [Eyevinn/vast-info](https://github.com/Eyevinn/vast-info)  - Parse a VAST or VMAP to show valuable information in a readable format - Eyevinn/vast-info
* [SCTE-104/35 and Beyond: A Look at Ad Insertion in an OTT World](https://www.tvtechnology.com/opinions/scte10435-and-beyond-a-look-at-ad-insertion-in-an-ott-world)  - Ad Insertion is a very important part of many video delivery systems because of the monetization aspect—it generates revenue!
* [Understanding Real-time Bidding for AVOD Services](https://medium.com/@eyevinntechnology/understanding-real-time-bidding-for-avod-services-861ebfa8bd13)  - We have in previous blog articles described the principles behind server-side ad-insertion and described some of the challenges with it as…
* [Understanding Server-Side Dynamic Ad Insertion](https://medium.com/@eyevinntechnology/understanding-server-side-dynamic-ad-insertion-d7ed90e34aa2)  - In this post we’re explaining the principles behind Server-Side Dynamic Ad Insertion technology. If you are already familiar with video…

## Vendors
*Video indurstry's various vendors products and documentations.*

* [switch media adease](https://www.switch.tv/mediahq/adease/)  - 
* [switch media live2vod](https://www.switch.tv/mediahq/live2vod/)  - 
* [switch media mediahq](https://www.switch.tv/mediahq/)  - 
* [switch media universal player](https://www.switch.tv/mediahq/universal-player/)  - 

### Dolby
*Dolby specs, libraries, examples, and tools.*
[back to top](#readme) 

* [Dolby Professional Loudness Suite](https://www.dolby.com/us/en/technologies/dolby-professional-loudness-solutions.pdf)  - 
* [Dolby Vision for Content Creators | Dolby Laboratories](https://www.dolby.com/us/en/technologies/dolby-vision/dolby-vision-for-creative-professionals.html)  - The Dolby Vision integrated workflow gives you the tools needed to efficiently create wide color gamut and high dynamic range content and ensures that the look you create in the color suite stays true when experienced across across a multitude of devices. With Dolby Vision high dynamic range imaging, you get bolder highlights and incredible contrast. That means greater sharpness, depth, and more detailed shadows to expand your storytelling possibilities like never before.
* [Hybrik API Reference](https://docs.hybrik.com/api/v1/HybrikAPI.html?#getting-started)  - 
* [dolby-vision-streams-within-the-http-live-streaming-format](https://www.dolby.com/us/en/technologies/dolby-vision/dolby-vision-streams-within-the-http-live-streaming-format-v2.0.pdf)  - 
* [hybrik/hybrik-samples](https://github.com/hybrik/hybrik-samples)  - Hybrik Samples.

## QoE
*QoE & Analytics tools, libraries, and resources.*

* [Collection of VMAF Resources](https://streaminglearningcenter.com/blogs/collection-of-vmaf-resources.html)  - A colleague asked for some resources relating to VMAF. Rather than answer in an email I thought I would create a post around it. Some of these are from Netflix, most from me (Jan Ozer). I’ve broken the items into three groups; Computing VMAF, Using VMAF, and About VMAF. I hope you find this collection useful.…
* [JNoDuq/videobench](https://github.com/JNoDuq/videobench)  - VMAF PSNR Bitrate Analyzer.
* [Netflix/vmaf](https://github.com/Netflix/vmaf/)  - Perceptual video quality assessment based on multi-method fusion. - Netflix/vmaf
* [Quality of Experience in Streaming](https://medium.com/@eyevinntechnology/quality-of-experience-in-streaming-5c25355a4111?source=userActivityShare-94bccb50d11-1559724940&_branch_match_id=664741478927428385)  - In Eyevinn Technology’s ambition to broader our sharing of knowledge we now expand this with addressing quality. In today’s landscape of…
* [The Challenge to Maintain and Translate Creative Visual Ideas to Everyone’s Viewing Devices](https://medium.com/@eyevinntechnology/the-challenge-to-maintain-and-translate-creative-visual-ideas-to-everyones-viewing-devices-a88e1a841439)  - Many articles have already been posted drawing conclusions on what went wrong with the visual quality of a very popular TV show that was…
* [Toward A Practical Perceptual Video Quality Metric](https://medium.com/netflix-techblog/toward-a-practical-perceptual-video-quality-metric-653f208b9652)  - measuring video quality accurately at scale
* [VMAF: The Journey Continues](https://medium.com/netflix-techblog/vmaf-the-journey-continues-44b51ee9ed12)  - by Zhi Li, Christos Bampis, Julie Novak, Anne Aaron, Kyle Swanson, Anush Moorthy and Jan De Cock
* [Video Bench — How measure your video quality easily](https://medium.com/@jnoduq/video-bench-how-measure-your-video-quality-easily-85a0feb8f6e2)  - Introduction
* [Video Quality Assessment](https://medium.com/@eyevinntechnology/video-quality-assessment-34abd35f96c0?source=userActivityShare-94bccb50d11-1560983815&_branch_match_id=670021582869771680)  - In Eyevinn’s initiative to share our knowledge around quality we continue with addressing video quality assessment; from both a subjective…
* [bavc/qctools](https://github.com/bavc/qctools)  - 
* [crunchyroll/objective_perceptual_analysis](https://github.com/crunchyroll/objective_perceptual_analysis)  - 
* [cta-wave/R4WG20-QoE-Metrics](https://github.com/cta-wave/R4WG20-QoE-Metrics)  - Issue tracking repository for the R4-Wg20 QoE Initiative - cta-wave/R4WG20-QoE-Metrics

## Tools
*Streaming video tools and resources to make life easier.*

* [A Docker container with the video streaming tools you need](https://medium.com/@eyevinntechnology/a-docker-container-with-the-video-streaming-tools-you-need-b8319e98f36a)  - As a video streaming technician there are a number of tools that you find yourself using on a daily basis. Wouldn’t it be handy if all…
* [AKSHAYUBHAT/DeepVideoAnalytics](https://github.com/AKSHAYUBHAT/DeepVideoAnalytics)  - A distributed visual search and visual data analytics platform. - AKSHAYUBHAT/DeepVideoAnalytics
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
* [Eyevinn/streaming-analyzer](https://github.com/Eyevinn/streaming-analyzer)  - Analyze and visualize HTTP ABR streams.
* [Eyevinn/toolbox](https://github.com/Eyevinn/toolbox)  - A set of Docker containers with Streaming tools.
* [Eyevinn/vod-to-live.js](https://github.com/Eyevinn/vod-to-live.js)  - NPM library for HLS VOD to Live.
* [Inca — Message Tracing and Loss Detection For Streaming Data @Netflix](https://link.medium.com/Lu3GnIPeg0)  - At Netflix, our real-time data infrastructure have embraced the multi-cluster Kafka architecture and Flink powered stream processing…
* [Kthulu120/liquid_dl](https://github.com/Kthulu120/liquid_dl)  - Liquid-dl is a simple tool for utlities such as FFMPEG, youtube-dl, and scdl. It provides a simple framework with simple point and click options allowing users to just click on what they need and u...
* [Marcos-A/STRCleaner](https://github.com/Marcos-A/STRCleaner)  - Script that extracts all the text from a subtitles file ignoring time indications, HTML tags and other alien info. - Marcos-A/STRCleaner
* [Open Broadcaster Software | OBS](https://obsproject.com/)  - OBS (Open Broadcaster Software) is free and open source software for video recording and live streaming. Stream to Twitch, YouTube and many other providers or record your own videos with high quality H264 / AAC encoding.
* [Stream Analyzer - ts analyzer, stream validation, ETSI TR 101 290 | Elecard: Video Compression Guru ](https://www.elecard.com/products/video-analysis/stream-analyzer)  - Professional Video Analysis Tool For Syntax Analysis Of Encoded Media Streams. Operates With MPEG-2 PS/TS, VES and MP4 Files. Automation, batch execution via Command Line Interface. Check your multiplexer
* [ZaifSenpai/Batch-Py-Remux](https://github.com/ZaifSenpai/Batch-Py-Remux)  - Convert mkv video to hevc (h.265).
* [awslabs/aws-stale-playlist-detector](https://github.com/awslabs/aws-stale-playlist-detector)  - The Stale Playlist Detector (SPD) is a tool to monitor live HLS origin endpoints for changing playlists. The Stale Playlist Detector (SPD) will use data in the top-level playlist, the child playlis...
* [bcpierce00/unison](https://github.com/bcpierce00/unison)  - Unison file synchronizer.
* [coopernurse/nginx-s3-proxy](https://github.com/coopernurse/nginx-s3-proxy)  - nginx compiled with aws-auth support, suitable for S3 reverse proxy usage - coopernurse/nginx-s3-proxy
* [estliberitas/node-thumbnails-webvtt](https://github.com/estliberitas/node-thumbnails-webvtt)  - Video thumbnail generator generating WebVTT spec file - estliberitas/node-thumbnails-webvtt
* [gnolizuh/BLSS](https://github.com/gnolizuh/BLSS)  - NGINX-based Live Media Streaming Server.
* [gpac/gpac](https://github.com/gpac/gpac)  - GPAC main code repository.
* [gpac/mp4box.js](https://github.com/gpac/mp4box.js)  - JavaScript version of GPAC's MP4Box tool.
* [jkarthic-akamai/ABR-Broadcaster](https://github.com/jkarthic-akamai/ABR-Broadcaster)  - A real time encoder for Adaptive Bitrate Broadcast - jkarthic-akamai/ABR-Broadcaster
* [liwf616/awesome-live-stream](https://github.com/liwf616/awesome-live-stream)  - Webrtc && Nginx && DASH && Quic 学习资料收集，持续更新中.
* [mar10/wsgidav](https://github.com/mar10/wsgidav)  - A generic and extendable WebDAV server based on WSGI - mar10/wsgidav
* [mifi/lossless-cut](https://github.com/mifi/lossless-cut)  - 
* [minio/minio](https://github.com/minio/minio)  - MinIO is a high performance object storage server compatible with Amazon S3 APIs - minio/minio
* [obsproject/obs-studio](https://github.com/obsproject/obs-studio)  - OBS Studio - Free and open source software for live streaming and screen recording - obsproject/obs-studio
* [realeyes-media/alpine-bento-ffmpeg](https://github.com/realeyes-media/alpine-bento-ffmpeg)  - Alpine Linux with FFMPEG, Bento, and PM2.
* [realeyes-media/alpine-node-video-multitool](https://github.com/realeyes-media/alpine-node-video-multitool)  - Contribute to realeyes-media/alpine-node-video-multitool development by creating an account on GitHub.
* [schedules/dl](https://github.com/schedules/dl)  - Node.js DASH and HLS downloader. 
* [slhck/ffmpeg-bitrate-stats](https://github.com/slhck/ffmpeg-bitrate-stats)  - Calculate bitrate statistics using FFmpeg
* [slhck/ffmpeg-debug-qp](https://github.com/slhck/ffmpeg-debug-qp)  - FFmpeg Debug Script for QP Values
* [slhck/ffmpeg-quality-metrics](https://github.com/slhck/ffmpeg-quality-metrics)  - Calculate quality metrics with FFmpeg (SSIM, PSNR, VMAF)
* [slhck/scenecut-extractor](https://github.com/slhck/scenecut-extractor)  - Extract scenecuts from video files using ffmpeg
* [video-dev/vtt.js](https://github.com/video-dev/vtt.js)  - A JavaScript implementation of the WebVTT specification - video-dev/vtt.js
* [watson-developer-cloud/text-to-speech-nodejs](https://github.com/watson-developer-cloud/text-to-speech-nodejs)  - :speaker: Sample Node.js Application for the IBM Watson Text to Speech Service - watson-developer-cloud/text-to-speech-nodejs

## DRM
*DRM tools, documentations, and resources.*

* [Content Protection for HLS with AES-128 Encryption](https://www.theoplayer.com/blog/content-protection-for-hls-with-aes-128-encryption)  - We will outline the most popular method for content protection with the HTTP Live Streaming (HLS) protocol: AES-128 content encryption.
* [CrackerCat/video_decrypter](https://github.com/CrackerCat/video_decrypter)  - Decrypt video from a streaming site with MPEG-DASH Widevine DRM encryption. - CrackerCat/video_decrypter
* [Digital Rights Management (DRM) – Everything you need to know](https://bitmovin.com/digital-rights-management-everything-to-know/)  - 
* [Encryption & DRM with Multiple Keys — Unified Streaming](https://docs.unified-streaming.com/documentation/package/multiple-keys.html)  - DRM with multiple keys for Unified Packager
* [HEVC DRM Market Update](https://go.buydrm.com/thedrmblog/hevc-drm-market-update)  - Since time eternal, the streaming industry has toiled with and extolled the virtues of CODECs and their key enablement of the entire digital video experience. Now comes the latest candy in the increasingly large bowl, H.265 (MPEG-H Part 2) or as it’s more commonly known. HEVC.
* [Secure HLS streaming using DRM encryption](https://www.wowza.com/docs/how-to-secure-apple-hls-streaming-using-drm-encryption)  - Protect live and on-demand HLS streaming using DRM encryption in Wowza Streaming Engine.
* [Securing OTT Content — DRM](https://medium.com/@eyevinntechnology/securing-ott-content-drm-1af2c08fdd31?source=userActivityShare-94bccb50d11-1560983518&_branch_match_id=670020366479331042)  - Written by: Boris Asadanin, Streaming Media Consultant and Partner at Eyevinn Technology
* [draft-pantos-hls-rfc8216bis-00 - HTTP Live Streaming 2nd Edition](https://tools.ietf.org/html/draft-pantos-hls-rfc8216bis-00#section-5.1)  - 
* [shengbinmeng/dash-drm](https://github.com/shengbinmeng/dash-drm)  - Demos of MPEG-DASH and DRM.
* [videojs/aes-decrypter](https://github.com/videojs/aes-decrypter)  - Contribute to videojs/aes-decrypter development by creating an account on GitHub.

## Testing
*Video streaming testing tools and helpers.*

* [4K Media | Free Ultra-HD / HDR / HLG / Dolby Vision 4K Video Demos](https://4kmedia.org/)  - Uncompressed 4K demos, samples, and trailers, to show off your new ultra-HD (2160p) HDR/HLG/Dolby Vision television or monitor.
* [Automated Testing on Devices](https://medium.com/netflix-techblog/automated-testing-on-devices-fc5a39f47e24)  - key concepts and infrastructure
* [DASH & HLS Sample Streams](https://bitmovin.com/mpeg-dash-hls-examples-sample-streams/)  - 
* [HTTP Live Streaming (HLS) - Artillery.io Docs](https://artillery.io/docs/plugin-hls/)  - 
* [Xiph.org :: Test Media](https://media.xiph.org/)  - 
* [artilleryio/artillery-plugin-hls](https://github.com/artilleryio/artillery-plugin-hls)  - Load test HTTP Live Streaming (HLS) servers with Artillery 🎥 - artilleryio/artillery-plugin-hls
* [bengarney/list-of-streams](https://github.com/bengarney/list-of-streams)  - Community list of public test streams for HLS and DASH. - bengarney/list-of-streams
* [video-dev/streams](https://github.com/video-dev/streams)  - A repository of shared streams - no media uploads.

## Community
*Video developers community, slack groups, conferences, meetups*


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
* [Fastly compared to Amazon CloudFront ](https://www.cdnoverview.com/compare/fastly-vs-amazon-cloudfront/)  - Compare CDN features and pricing on CDNOverview.com
* [How to use DASH and HLS Adaptive Streaming with AWS S3 and Cloudfront](https://bitmovin.zendesk.com/hc/en-us/articles/115001609634-How-to-use-DASH-and-HLS-Adaptive-Streaming-with-AWS-S3-and-Cloudfront)  - Bitmovin integrates DASH and HLS adaptive streaming seamlessly into your AWS workflows. The Bitmovin encoding service could be configured to use an AWS S3 bucket as input and output for your DASH a...
* [Lambda Edge Tutorial](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works-tutorial.html)  - This tutorial shows you how to get started with Lambda@Edge by helping you create and add a sample Node.js function that runs in CloudFront. The example that we walk through adds HTTP security headers to a response, which can improve security and privacy for a website. (That said, you don’t need a website for this walkthrough; we simply add security headers to a response when CloudFront retrieves a file.)
* [Lambda@Edge Design Best Practices | Amazon Web Services](https://aws.amazon.com/blogs/networking-and-content-delivery/lambdaedge-design-best-practices/)  - Lambda@Edge transforms CloudFront into a highly programmable CDN with serverless compute capabilities closer to your viewers around the world. This blog is the first in a series that explains best practices associated with using Lambda@Edge functions to customize your content delivery.
* [OTT Content Delivery– CDN Alternatives](https://medium.com/@eyevinntechnology/ott-content-delivery-cdn-alternatives-cafe75dab71d?source=userActivityShare-94bccb50d11-1560983135&_branch_match_id=670018733519578135)  - Introduction

## HDR10, HLG, Dolby Vision
*HDR tools, learning, documentations, and resources.*

* [Encode HDR with VP9](https://developers.google.com/media/vp9/hdr-encoding)  - Hands on tutorial of using ffmpeg to do hdr encoding
* [Frequently Asked Questions on High Dynamic Range and Hybrid Log-Gamma](https://downloads.bbc.co.uk/rd/pubs/papers/HDR/BBC_HDRTV_FAQ.pdf)  - FAQ regarding HDR by BBC R&D
* [HLG vs PQ Systems for HDR Television](https://www.displaydaily.com/article/display-daily/hlg-vs-pq-systems-for-hdr-television)  - Article explaining hlg vs pq in depth.
* [High Dynamic Range Television and Hybrid Log-Gamma - BBC R&D](https://www.bbc.co.uk/rd/projects/high-dynamic-range)  - BBC R&D HDR project page.
* [Perceptual Quantiser (PQ) to Hybrid Log-Gamma (HLG) Transcoding](https://downloads.bbc.co.uk/rd/pubs/papers/HDR/BBC_HDRTV_PQ_HLG_Transcode_v2.pdf)  - In depth break down on converting from pq to hlg
* [UHD & HDR Overview](https://www.smpte.org/sites/default/files/users/user27446/HDR%20SMPTE%20Presentation%20March%2021%2C%202017%20V2.compressed.pdf)  - SMPTE Presentation
* [Use of Look-Up Tables (LUTs) in FFmpeg](https://downloads.bbc.co.uk/rd/pubs/papers/HDR/BBC_HDRTV_Use_of_LUTs_FFmpeg.pdf)  - How to use luts with ffmpeg for converting between differnt hdr encodes
* [Vittorio Giovara - Color Me Intrigued: A Jaunt Through Color Technology in Video](https://www.youtube.com/watch?v=XMnvY7a4-As&feature=share)  - This talk aims to shed light on colorspaces - what they are, how and why they work, why we should care about handling edge cases properly. Starting with hist...
* [bbc/qtff-parameter-editor](https://github.com/bbc/qtff-parameter-editor)  - QuickTime file parameter editor for modifying transfer function, colour primary and matrix characteristics.
* [id3as/ffmpeg-libvpx-HDR-static](https://github.com/id3as/ffmpeg-libvpx-HDR-static)  - A script to build a static binary of FFmpeg optimised for libvpx (HDR 10bit) encoding.


### Contributing

Please take a quick look at the [contribution guidelines](https://github.com/krzemienski/awesome-video/blob/master/.github/CONTRIBUTING.md) first. If you see a package or project here that is no longer maintained or is not a good fit, please submit a pull request to improve this file. Thank you to all [contributors](https://github.com/krzemienski/awesome-video/graphs/contributors); you rock!!