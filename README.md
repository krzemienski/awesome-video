# Awesome Video [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
 
<!-- 

PLEASE DO NOT UPDATE THIS FILE, UPDATE CONTENTS.JSON INSTEAD. THANK YOU :-)

 -->





### Contents

- [Introduction](#intro)
- [Learning](#learning)
- [HLS](#hls)
- [DASH](#dash)
- [Encoding](#encoding)
- [Reading](#reading)
- [Specs & Standards](#specs-standards)
- [Players](#players)
- [FFMPEG](#ffmpeg)
- [Audio](#audio)
- [Subtitles & Closed Captions](#subtitle)
- [HEVC](#hevc)
- [Ads](#ads)
- [Roku](#roku)
- [Dolby](#dolby)
- [QoE](#qoe)
- [Tools](#tools)
- [DRM](#drm)
- [Testing](#testing)
- [Talks and Presentations](#talks)
- [Books](#books)
- [CDN](#cdn)

## Introduction
*What's video?*

* [A short history of video coding](https://www.slideshare.net/vcodex/a-short-history-of-video-coding?from_m_app=ios)  - From H.261 to H.265
* [digital_video_introduction: A hands-on introduction to video technology: image, video, codec (av1, vp9, h265) and more (ffmpeg encoding).](https://github.com/leandromoreira/digital_video_introduction)  - A gentle introduction to video technology, although it's aimed at software developers / engineers, we want to make it easy for anyone to learn.
* [eyevinn/streaming-onboarding](https://github.com/Eyevinn/streaming-onboarding)  - New to streaming and don't know where to start? This is the place for you!

## Learning
*An awesome list of learning video streaming resources.*

* [Adding Alternate Media to a Playlist | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/adding_alternate_media_to_a_playlist)  - 
* [Apple LLHLS + LL-CMAF](https://docs.google.com/presentation/d/1ZwqWcweR5SqeMBRmJjSukWaHbpdPy-EPYvJCS23_n3U/edit?usp=sharing)  - 
* [Back to Basics: Encoding Definition and Adaptive Bitrate](https://bitmovin.com/encoding-definition-bitrates/?utm_campaign=Newsletter&utm_medium=email&_hsenc=p2ANqtz-8MPFxhR7snQrxPYM7Bl3UTEMgOh5ZXoDQCHjLl9lkskqE0IfBhEuz3us39Br-lvA_CnyNmQl6L5wqO6iKOfAJ8HznenQ&_hsmi=79678208&utm_content=79677632&utm_source=hs_email&hsCtaTracking=b8eb0e0a-f292-435e-8b99-719b75d81412%7C367afa65-d810-4c2e-aa2c-c87e897a8942)  - 
* [Create your own video streaming server with Linux | Opensource.com](https://opensource.com/article/19/1/basic-live-video-streaming-server)  - 
* [Creating A Production Ready Multi Bitrate HLS VOD stream](https://docs.peer5.com/guides/production-ready-hls-vod/)  - 
* [Creating a Master Playlist | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/creating_a_master_playlist#overview)  - 
* [Experiences with the AV1 codec, how it works, how to encode decode](https://docs.google.com/presentation/d/12_Vewc0SDpB1FycflfT4us9eipRCy0HWJVSaDMDifRs/edit?usp=sharing)  - 
* [FFmpeg and how to use it wrong | VideoBlerg](https://videoblerg.wordpress.com/2017/11/10/ffmpeg-and-how-to-use-it-wrong/)  - 
* [Guide to Mobile Video Streaming with HLS](https://mux.com/blog/mobile-hls-guide/)  - 
* [HLS Authoring Specification for Apple Devices | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/hls_authoring_specification_for_apple_devices)  - 
* [HLS adaptive streaming tutorial with CloudFront & JW Player](https://www.miracletutorials.com/hls-adaptive-streaming-tutorial-with-cloudfront-jw-player/)  - 
* [HOW TO: View an HLS Stream in QuickTime or VLC](https://softron.zendesk.com/hc/en-us/articles/207694617-HOW-TO-View-an-HLS-Stream-in-QuickTime-or-VLC?mobile_site=true)  - 
* [HTTP Live Streaming: HLS Player for Android | Toptal](https://www.toptal.com/apple/introduction-to-http-live-streaming-hls)  - 
* [How To Setup Nginx For HLS Video Streaming On Centos 7](https://dev.to/samuyi/how-to-setup-nginx-for-hls-video-streaming-on-centos-7-3jb8)  - 
* [How video engineers might be able to help out with wild bush fires](https://docs.google.com/presentation/d/1yiVEOq2rvtFynP1tLdJj7pBWkAEiE9g8BMaoryxRVrk/edit?usp=sharing)  - 
* [How video streaming works on the web: An introduction](https://medium.com/canal-tech/how-video-streaming-works-on-the-web-an-introduction-7919739f7e1)  - 
* [Internet Video Streaming part 1](https://medium.com/@eyevinntechnology/internet-video-streaming-abr-part-1-b10964849e19?source=userActivityShare-94bccb50d11-1559723768&_branch_match_id=664736558865703297)  - 
* [Internet Video Streaming? ABR part 2](https://medium.com/@eyevinntechnology/internet-video-streaming-abr-part-2-dbce136b0d7c?source=userActivityShare-94bccb50d11-1559723862&_branch_match_id=664736952377004405)  - 
* [Live Playlist (Sliding Window) Construction | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/live_playlist_sliding_window_construction)  - 
* [Live Video Transmuxing/Transcoding: FFmpeg vs TwitchTranscoder, Part I](https://blog.twitch.tv/en/2017/10/10/live-video-transmuxing-transcoding-f-fmpeg-vs-twitch-transcoder-part-i-489c1c125f28/)  - 
* [Live Video Transmuxing/Transcoding: FFmpeg vs TwitchTranscoder, Part II](https://blog.twitch.tv/live-video-transmuxing-transcoding-ffmpeg-vs-twitchtranscoder-part-ii-4973f475f8a3?source=userActivityShare-94bccb50d11-1561003748&_branch_match_id=670105191114382351&gi=fd8d504494f4)  - 
* [OTT Content Delivery](https://medium.com/@eyevinntechnology/ott-content-delivery-b43a35ef24f6)  - 
* [OTT Content Delivery Multi CDN](https://medium.com/@eyevinntechnology/ott-content-delivery-multi-cdn-8cd90ad2628a?source=userActivityShare-94bccb50d11-1560983307&_branch_match_id=670019455010399744)  - 
* [Server-less Video Backend - Eyevinn Technology - Medium](https://medium.com/@eyevinntechnology/server-less-video-backend-1a142d1d2ba)  - 
* [The structure of an MPEG-DASH MPD - Brendan Long](https://www.brendanlong.com/the-structure-of-an-mpeg-dash-mpd.html)  - 
* [Understanding the HTTP Live Streaming Architecture | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/understanding_the_http_live_streaming_architecture)  - 
* [Using Tensor flow machine learning for audience ratings](https://docs.google.com/presentation/d/1NAqYWmFOwxJEacZCuPLdX0mRNRFPFgeRbsm22EaxerU/edit?usp=sharing)  - 
* [Video Encoding Compression and Resolutions](https://medium.com/@eyevinntechnology/chessboard-for-beginners-video-encoding-compression-and-resolutions-bcefe04fa639)  - 
* [Video on Demand Playlist Construction | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/video_on_demand_playlist_construction)  - 
* [Video on Demand to Linear Live streaming auto translation VOD2Live](https://docs.google.com/presentation/d/1Ua76BBaZKtTmaZrlfM_eG0vwz0ZAqPIjreCSfB4qFQQ/edit?usp=sharing)  - 
* [WebAssembly on the CDN Edge](https://docs.google.com/presentation/d/1sonEk2neNVBcy8EzieUjWCNzj5SXN7dk-unkR_lpl8k/edit?usp=sharing)  - 
* [Xdebug, useful for anyone manipulating video with PHP](https://docs.google.com/presentation/d/15560aTv054w6bXKQ9gmBCE8gYwgtXhaPOHS1JcqTofk/edit?usp=sharing)  - 
* [bash scripts to create VOD HLS stream with ffmpeg almighty (tested on Linux and OS X)](https://gist.github.com/mrbar42/ae111731906f958b396f30906004b3fa)  - 
* [create-DASH-HLS](https://github.com/matmoi/create-DASH-HLS/)  - A tutorial to generate fMp4 files compatible with dash and HLS
* [matmoi/create-DASH-HLS: A tutorial to generate fMp4 files compatible with dash and HLS](https://github.com/matmoi/create-DASH-HLS)  - 

## HLS
*HLS tools, libraries, and resources.*

* [Advances in HTTP Live Streaming WWDC](https://devstreaming-cdn.apple.com/videos/wwdc/2017/504op4c3001w2f222/504/504_advances_in_http_live_streaming.pdf)  - 
* [AirPlay2 Example Code](https://developer.apple.com/documentation/avfoundation/airplay_2/integrating_airplay_for_long-form_video_apps)  - 
* [AirPlay2 WWDC 19 Slides](https://devstreaming-cdn.apple.com/videos/wwdc/2019/507fk9wyls0np6piwk/507/507_hls_authoring_for_airplay_2_video.pdf)  - 
* [Eyevinn/Hls-download](https://github.com/Eyevinn/hls-download)  - 
* [Eyevinn/hls-origin-scripts](https://github.com/Eyevinn/hls-origin-scripts)  - 
* [Eyevinn/hls-playlist-parser](https://github.com/Eyevinn/hls-playlist-parser)  - 
* [Eyevinn/hls-relay](https://github.com/Eyevinn/hls-relay)  - 
* [Eyevinn/hls-ts-analyzer](https://github.com/Eyevinn/hls-ts-analyzer)  - 
* [Eyevinn/hls-ts-js](https://github.com/Eyevinn/hls-ts-js)  - 
* [Eyevinn/manifestparser](https://github.com/Eyevinn/manifestparser)  - 
* [GitHub - Eyevinn/vod-to-live: A python library to generate Live HLS from VOD](https://github.com/Eyevinn/vod-to-live)  - 
* [HLS and Fragmented MP4 | HTTP Live Streaming](https://hlsbook.net/hls-fragmented-mp4/)  - At WWDC 2016, Apple announced support for fragmented MP4 (fMP4) as an alternative to MPEG-TS, which prior to their announcement was the only supported format.
* [HLS | Bento4](https://www.bento4.com/developers/hls/)  - 
* [HLSCore Swift HLS lib](https://github.com/fcanas/HLSCore)  - 
* [HLSDownloader](https://github.com/nmrony/hlsdownloader)  - Downloads m3u8 playlist and TS chunks for a given playlist URL.
* [HLSDownloader Swift](https://github.com/qi-shun-wang/HLSDownloader)  - 
* [Introducing Low-Latency HLS - WWDC 2019 - Videos - Apple Developer](https://developer.apple.com/videos/play/wwdc2019/502)  - 
* [Protocol Extension for Low-Latency HLS (Preliminary Specification) | Apple Developer Documentation](https://developer.apple.com/documentation/http_live_streaming/protocol_extension_for_low-latency_hls_preliminary_specification#3291001)  - 
* [Validating HLS](https://devstreaming-cdn.apple.com/videos/wwdc/2016/510ndmh9wkcvzneegv2/510/510_validating_http_live_streams.pdf)  - 
* [denex/hls-downloader](https://github.com/denex/hls-downloader)  - 
* [dhairav/URLSessionHLSDownload: A swift 3 implementation for downloading HLS content and play it back using native AVPlayer](https://github.com/dhairav/URLSessionHLSDownload)  - 
* [epiclabs-io/hls-analyzer: Analyzer for HTTP Live Streams (HLS) content](https://github.com/epiclabs-io/hls-analyzer)  - 
* [flavioribeiro/nginx-audio-track-for-hls-module: Nginx module that generates audio track for HTTP Live Streaming (HLS) streams on the fly.](https://github.com/flavioribeiro/nginx-audio-track-for-hls-module)  - 
* [flavioribeiro/nginx-vod-module-fmp4-hls: Play fragmented mp4's on HLS using nginx-vod-module](https://github.com/flavioribeiro/nginx-vod-module-fmp4-hls)  - 
* [globocom/hlsclient: Python HLS Client](https://github.com/globocom/hlsclient)  - 
* [hls-fetch](https://github.com/osklil/hls-fetch)  - 
* [iheartradio/open-m3u8: Open Source m3u8 Parser](https://github.com/iheartradio/open-m3u8)  - 
* [imsanthosh/HLS-Stream-health-monitoring-tool: HLS stream health monitoring utility tool provides an report of live HLS stream. This utility ...](https://github.com/imsanthosh/HLS-Stream-health-monitoring-tool)  - 
* [lcy0321/m3u8-downloader: Download the ts files according to the given m3u8 file.](https://github.com/lcy0321/m3u8-downloader)  - 
* [m3u8-parser](https://github.com/videojs/m3u8-parser)  - 
* [majamee/arch-ffmpeg-gpac: A ready-prepared video transcoding pipeline to create DASH/ HLS compatible video files & playlists](https://github.com/majamee/arch-ffmpeg-gpac)  - 
* [mifi/hls-vod: HTTP Live Streaming with on-the-fly encoding of any video file for Web/Apple TV/iPhone/iPad/iPod](https://github.com/mifi/hls-vod)  - 
* [morsel Swift HLS library](https://github.com/krad/morsel)  - 
* [nmrony/hlsdownloader-cli: Downloads HLS Playlist file and TS chunks using Terminal](https://github.com/nmrony/hlsdownloader-cli)  - 
* [openHPI/nginx-hls-analyzer: Fork of fmsloganalyzer to adapt it for HLS streaming analyzes with nginx](https://github.com/openHPI/nginx-hls-analyzer)  - 
* [r-plus/HLSion: HTTP Live Streaming (HLS) download manager to offline playback.](https://github.com/r-plus/HLSion)  - 
* [rounce/nginx-hls-module: Smooth Streaming Module fork](https://github.com/rounce/nginx-hls-module)  - 
* [selsta/hlsdl: C program to download VoD HLS (.m3u8) files GitHub:](https://github.com/selsta/hlsdl)  - 
* [shrimpgo/video-downloader](https://github.com/shrimpgo/video-downloader)  - 
* [tjenkinson/mock-hls-server: Fake a live/event HLS stream from a VOD one. Useful for testing.](https://github.com/tjenkinson/mock-hls-server)  - 
* [yuhuili-lab/Tide](https://github.com/yuhuili-lab/Tide)  - 
* [zhaiweiwei/nginx-hls](https://github.com/zhaiweiwei/nginx-hls)  - 
* [﻿alfg/docker-nginx-rtmp: 🐋 A Dockerfile for nginx-rtmp-module + FFmpeg from source with basic settings for streaming HLS. Built on Alpine Li...](https://github.com/alfg/docker-nginx-rtmp)  - 

## DASH
*DASH tools, libraries, and resources.*

* [DASH-IF Conformance Software](https://github.com/Dash-Industry-Forum/DASH-IF-Conformance)  - 
* [DASH-IF DASH Live Source Simulator](https://github.com/Dash-Industry-Forum/dash-live-source-simulator)  - 
* [DASH-IF Interoperability: Guidelines for Implementations](https://dashif.org/docs/DASH-IF-IOP-v4.3.pdf)  - 
* [Dash-Industry-Forum/dash.js](https://github.com/Dash-Industry-Forum/dash.js)  - 
* [Eyevinn/dash-validator-js](https://github.com/Eyevinn/dash-validator-js)  - 
* [Eyevinn/docker-2dash: A Docker container to pre-package MPEG DASH on demand content](https://github.com/Eyevinn/docker-2dash)  - 
* [Eyevinn/vp9-dash](https://github.com/Eyevinn/vp9-dash)  - 
* [ISO Segment Validator](https://github.com/Dash-Industry-Forum/ISOSegmentValidator)  - ISO BMFF, DASH, CMAF and HbbTV - DVB segment validation conformance
* [carlanton/mpd-tools: DASH MPD tools for Java](https://github.com/carlanton/mpd-tools)  - 
* [caststack/python-mpegdash](https://github.com/caststack/python-mpegdash)  - 
* [dash-proxy](https://github.com/Viblast/dash-proxy)  - Dash proxy is a tool that allows for easy downloading or mirroring of remote MPEG-DASH streams.
* [djvergad/dash](https://github.com/djvergad/dash)  - 
* [docker-dash-packager](https://github.com/Eyevinn/docker-dash-packager)  -  Docker container for an open source MPEG DASH packager
* [libdash](https://github.com/bitmovin/libdash)  - 
* [mahbubcseju/MPEG-DASH-Downloader](https://github.com/mahbubcseju/MPEG-DASH-Downloader)  - 
* [media-tools](https://github.com/Dash-Industry-Forum/media-tools)  - 
* [mp4dash | Bento4](https://www.bento4.com/documentation/mp4dash/)  - 
* [mpd-parser](https://github.com/videojs/mpd-parser)  - 
* [nickdesaulniers/combine-mpd](https://github.com/nickdesaulniers/combine-mpd)  - 
* [stultus/mp4-to-mpegdash-py](https://github.com/stultus/mp4-to-mpegdash-py)  - 
* [tchakabam/dash-proxy](https://github.com/tchakabam/dash-proxy)  - 
* [theolampert/dash-server](https://github.com/theolampert/dash-server)  - 
* [videojs/videojs-contrib-dash](https://github.com/videojs/videojs-contrib-dash)  - 

## Encoding
*Encoding tools, libraries, and resources.*

* [A Large-Scale Comparison of x264 x265 and libvpx](https://medium.com/netflix-techblog/a-large-scale-comparison-of-x264-x265-and-libvpx-a-sneak-peek-2e81e88f8b0f)  - Netflix Technology Blog.
* [Bento4 | Fast, Modern Tools and C++ Class Library for all your MP4 and DASH media format needs](https://www.bento4.com/)  - 
* [Introducing SVT-AV1: a scalable open-source AV1 framework](https://medium.com/netflix-techblog/introducing-svt-av1-a-scalable-open-source-av1-framework-c726cce3103a)  - 
* [avTranscoder/avTranscoder: C++ API for LibAV / FFMpeg](https://github.com/avTranscoder/avTranscoder)  - 
* [bfansports/CloudTranscode: Distributed videos and images encoding/transcoding using Amazon SFN, FFMpeg and ImageMagic](https://github.com/bfansports/CloudTranscode)  - 
* [bloc97/Anime4K](https://github.com/bloc97/Anime4K)  - 
* [cannonbeach/ott-packager](https://github.com/cannonbeach/ott-packager)  - 
* [demo-encoder](https://github.com/realeyes-media/demo-encoder/)  - A nodejs encoding system based on ffmpeg and configured to write HLS streaming files to S3
* [docker-bento4](https://github.com/alfg/docker-bento4)  - 
* [nytimes/video-presets](https://github.com/nytimes/video-presets)  - 
* [olaris / olaris-server](https://gitlab.com/olaris/olaris-server)  - 
* [ptrandev/swift-encoder: A fire-and-forget shell script that encodes multiple video and audio files with ffmpeg.](https://github.com/ptrandev/swift-encoder)  - 
* [realeyes-media/demo-encoder: A nodejs encoding system based on ffmpeg and configured to write HLS streaming files to S3](https://github.com/realeyes-media/demo-encoder)  - 
* [snickers/snickers: An open source alternative to the video cloud encoding services.](https://github.com/snickers/snickers)  - 

## Reading
*A list of reading articles, blogs, and newsletters for video streaming.*

* [9 Best Home Server Apps to Automate Media Management](https://www.smarthomebeginner.com/best-home-server-apps/)  - 
* [Battle of the Video Format: Comparing MKV vs MP4](https://bitmovin.com/mkv-vs-mp4/?utm_campaign=Newsletter&utm_medium=email&_hsenc=p2ANqtz--KSAyThG9MNeSt28DH4ARDp3E1ujyIxyFCr2Dlctl7XcrajMAhRv2exdRRtgAFkaGnNIV_oDJgUAFV9joOCsDy-Vh_sw&_hsmi=80348170&utm_content=80347861&utm_source=hs_email&hsCtaTracking=a4ecf824-05b6-41b1-b600-20a1cd5b0cf6%7C1853ebeb-bdae-4e36-b131-2fdf6e65a93d)  - 
* [Extracting contextual information from video assets](https://medium.com/netflix-techblog/extracting-contextual-information-from-video-assets-ee9da25b6008)  - 
* [IMF: A Prescription for Versionitis](https://medium.com/netflix-techblog/imf-a-prescription-for-versionitis-e0b4c1865c20)  - 
* [Inside MPEG's Ambitious Plan to Launch 3 Video Codecs in 2020](https://www.streamingmedia.com/Articles/Editorial/Featured-Articles/Inside-MPEGs-Ambitious-Plan-to-Launch-3-Video-Codecs-in-2020-134694.aspx)  - 
* [Server-less Just-in-Time Packaging with AWS Fargate and Unified Origin by Unified Streaming](https://medium.com/@eyevinntechnology/server-less-just-in-time-packaging-with-aws-fargate-and-unified-origin-by-unified-streaming-c1682dc051ca?source=userActivityShare-94bccb50d11-1559724204&_branch_match_id=664738392430917730)  - 
* [Server-less Just-in-Time Packaging with AWS Fargate and Unified Origin by Unified Streaming](https://medium.com/@eyevinntechnology/server-less-just-in-time-packaging-with-aws-fargate-and-unified-origin-by-unified-streaming-c1682dc051ca?source=userActivityShare-94bccb50d11-1560983627&_branch_match_id=670020794794030328)  - 
* [Streaming Live From the Battlefield: Military Video in 2019](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=135141)  - 
* [The Netflix Content Processing Pipeline](https://medium.com/netflix-techblog/the-netflix-imf-workflow-f45dd72ed700?source=userActivityShare-94bccb50d11-1568773157&_branch_match_id=702692448596112473)  - 
* [Video in the War Zone: The Current State of Military Streaming](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=101310)  - 

## Specs & Standards
*Latest offical specs and standards related to video streaming.*

* [HTTP Live Streaming 2nd Edition](https://tools.ietf.org/pdf/draft-pantos-hls-rfc8216bis-05.pdf)  - 
* [SCTE Dash SPEC](https://www.scte.org/SCTEDocs/Standards/ANSI_SCTE%20214-1%202015.pdf)  - 

## Players
*Client players, libraries, tools, and examples.*

* [A curated list of awesome resources for building Smart TV apps](https://github.com/vitalets/awesome-smart-tv)  - 
* [BrikerMan/BMPlayer: A video player for iOS, based on AVPlayer, support the horizontal, vertical screen. support adjust volume, brightness an...](https://github.com/BrikerMan/BMPlayer)  - 
* [Chromecast Receiver Docs](https://codelabs.developers.google.com/codelabs/cast-receiver/#0)  - 
* [DaMingShen/SUCacheLoader: AVPlayer缓存实现](https://github.com/DaMingShen/SUCacheLoader)  - 
* [Demystifying HTML5 Video Player - Eyevinn Technology - Medium](https://medium.com/@eyevinntechnology/demystifying-html5-video-player-e480846328f0)  - 
* [DeviLeo/DLGPlayer: A media player for iOS based on FFmpeg 4.0](https://github.com/DeviLeo/DLGPlayer)  - 
* [Eyevinn/abr-player-chrome](https://github.com/Eyevinn/abr-player-chrome)  - 
* [Eyevinn/av1-player](https://github.com/Eyevinn/av1-player)  - 
* [Eyevinn/channel-engine-multiview](https://github.com/Eyevinn/channel-engine-multiview)  - 
* [Eyevinn/docker-html5player](https://github.com/Eyevinn/docker-html5player)  - 
* [Eyevinn/eyevinn-player](https://github.com/Eyevinn/eyevinn-player)  - 
* [Eyevinn/ott-multiview](https://github.com/Eyevinn/ott-multiview)  - 
* [MPEGDASHPlayer/MPEGDASH-iOS-Player](https://github.com/MPEGDASHPlayer/MPEGDASH-iOS-Player)  - 
* [Ruffle](https://github.com/ruffle-rs/ruffle)  - 
* [StyleShare/HLSCachingReverseProxyServer](https://github.com/StyleShare/HLSCachingReverseProxyServer)  - 
* [SwitchMedia MediaHQ - SmartTV/CTV HbbTV player](https://www.switch.tv/mediahq/universal-player/)  - 
* [VeinGuo/VGPlayer: 📺 A simple iOS video player by Vein.](https://github.com/VeinGuo/VGPlayer)  - 
* [davidAgo4g/VideoPlayer-iOS: A library based on FFMPEG to play video files on iOS using OpenGLES and AudioQueue. Build with theos](https://github.com/davidAgo4g/VideoPlayer-iOS)  - 
* [googleads/google-media-framework-ios: The Google Media Framework (GMF) is a lightweight media player designed to make video playback and int...](https://github.com/googleads/google-media-framework-ios)  - 
* [googlecast/CastReceiver](https://github.com/googlecast/CastReceiver)  - 
* [hanton/HTY360Player: Open Source iOS 360 Degree Panorama Video Player.](https://github.com/hanton/HTY360Player)  - 
* [iina/iina: The modern video player for macOS.](https://github.com/iina/iina)  - 
* [imoreapps/ffmpeg-avplayer-for-ios-tvos: A tiny but powerful iOS and Apple TV OS av player framework that's based on the FFmpeg library.](https://github.com/imoreapps/ffmpeg-avplayer-for-ios-tvos)  - 
* [kodlian/TVVLCPlayer: TVVLCPlayer lets you integrate easily a powerfull video player with playback control views to your tvOS apps.](https://github.com/kodlian/TVVLCPlayer)  - 
* [libobjc/SGPlayer: A powerful media play framework for iOS, macOS, and tvOS.](https://github.com/libobjc/SGPlayer)  - 
* [lightspark/lightspark: An open source flash player implementation](https://github.com/lightspark/lightspark)  - 
* [masterjk/ios-avplayer-http-capture: iOS based application that embeds the AVPlayer and capture HTTP headers and send it back to the iOS appl...](https://github.com/masterjk/ios-avplayer-http-capture)  - 
* [nytimes/ios-360-videos: NYT360Video plays 360-degree video streamed from an AVPlayer on iOS.](https://github.com/nytimes/ios-360-videos)  - 
* [peak3d/inputstream.adaptive](https://github.com/peak3d/inputstream.adaptive)  - 
* [piemonte/Player: ▶️ video player in Swift, simple way to play and stream media on iOS/tvOS](https://github.com/piemonte/Player)  - 
* [renzifeng/ZFPlayer: Support customization of any player SDK and control layer(支持定制任何播放器SDK和控制层)](https://github.com/renzifeng/ZFPlayer)  - 
* [rokudev/videoplayer-channel: SceneGraph version of the SDK1 VideoPlayer Channel](https://github.com/rokudev/videoplayer-channel)  - 
* [sampotts/plyr: A simple HTML5, YouTube and Vimeo player](https://github.com/sampotts/plyr)  - 
* [tanersener/mobile-ffmpeg: FFmpeg for Android, iOS and tvOS](https://github.com/tanersener/mobile-ffmpeg)  - 
* [tjenkinson/media-element-syncer](https://github.com/tjenkinson/media-element-syncer)  - 
* [ustwo/videoplayback-ios: Swift AVPlayer wrapper using the VIPER architecture. Currently a work in progress](https://github.com/ustwo/videoplayback-ios)  - 
* [video-dev/hls.js: JavaScript HLS client using Media Source Extension](https://github.com/video-dev/hls.js)  - 
* [videojs/video.js: Video.js - open source HTML5 & Flash video player](https://github.com/videojs/video.js)  - 
* [videolan/vlc: VLC media player - All pull requests are ignored, please follow https://wiki.videolan.org/Sending_Patches_VLC/](https://github.com/videolan/vlc)  - 
* [vitoziv/VIMediaCache: Cache media file while play media using AVPlayer](https://github.com/vitoziv/VIMediaCache)  - 
* [xiewei-wayne/FFEngine.framework: FFEngine framework is a high performance player sdk for iOS based on ffmpeg.](https://github.com/xiewei-wayne/FFEngine.framework)  - 
* [xiewei-wayne/rtmp-video-player-for-ios: Based on FFEngine framework, a rtmp video player for apple iOS devices.](https://github.com/xiewei-wayne/rtmp-video-player-for-ios)  - 

## FFMPEG
*FFMPEG libraries, configs, tools, and examples.*

* [ CRF Guide (Constant Rate Factor in x264, x265 and libvpx)](http://slhck.info/video/2017/02/24/crf-guide.html)  - The Constant Rate Factor (CRF) is the default quality (and rate control) setting for the x264 and x265 encoders 
* [ElderByte-/docker-java-media: JRE 10 (Java 10) and media tools (ffmpeg)](https://github.com/ElderByte-/docker-java-media)  - 
* [FFmpeg/FFmpeg: Mirror of git://source.ffmpeg.org/ffmpeg.git](https://github.com/FFmpeg/FFmpeg)  - 
* [FFmpeg4Java 3.1.1-1.1](https://github.com/nextbreakpoint/ffmpeg4java)  - 
* [FallingSnow/h265ize: A node utility utilizing ffmpeg to encode videos with the hevc codec.](https://github.com/FallingSnow/h265ize)  - 
* [Generate MPEG-TS from file with ffmpeg](https://medium.com/@eyevinntechnology/generate-mpeg-ts-from-file-with-ffmpeg-7561181e6369?source=userActivityShare-94bccb50d11-1560983471&_branch_match_id=670020142756633081)  - 
* [How to generate a fmp4 hls live stream with FFMPEG](https://nomadyun.wordpress.com/2018/04/12/how-to-generate-a-fmp4-hls-live-stream-with-ffmpeg/)  - ffmpeg example command.
* [Loop file and generate multiple video bitrates muxed in MPEG-TS with ffmpeg](https://medium.com/@eyevinntechnology/loop-file-and-generate-multiple-video-bitrates-muxed-in-mpeg-ts-with-ffmpeg-85658d0b74bb?source=userActivityShare-94bccb50d11-1560983383&_branch_match_id=670019768959110835)  - 
* [awesome-ffmpeg](https://github.com/transitive-bullshit/awesome-ffmpeg)  - A curated list of awesome FFmpeg resources.
* [bcoudurier/FFmbc](https://github.com/bcoudurier/FFmbc)  - 
* [compile and install latest ffmpeg source as pkg](https://gist.github.com/krzemienski/e51a0b7a6ba77e616f954e516783270c#file-compile-and-install-latest-ffmpeg-source-sh-L2)  - 
* [cuda/ubuntu16.04/ffmpeg-gpu/Dockerfile master nvidia / container-images / samples GitLab](https://gitlab.com/nvidia/container-images/samples/blob/master/cuda/ubuntu16.04/ffmpeg-gpu/Dockerfile)  - 
* [ffmpeg and hardware acceleration of HEVC transcoding](https://superuser.com/questions/1295957/ffmpeg-and-hardware-acceleration-of-hevc-transcoding-on-mac)  - ffmpeg -hide_banner -h encoder=hevc_videotoolbox 
* [jrottenberg/ffmpeg: Docker build for FFmpeg on Ubuntu / Alpine / Centos 7 / Scratch](https://github.com/jrottenberg/ffmpeg)  - 
* [kokorin/Jaffree](https://github.com/kokorin/Jaffree)  - 
* [markus-perl/ffmpeg-build-script: The FFmpeg build script provides an easy way to build a static FFmpeg on OSX and Linux with non-free codecs...](https://github.com/markus-perl/ffmpeg-build-script)  - 
* [microshow/RxFFmpeg: 🔥RxFFmpeg 是基于 ( FFmpeg 4.0 + X264 + mp3lame + fdk-aac ) 编译的适用于 Android 平台的音视频编辑、视频剪辑的快速处理框架，包含以下功能（视频拼接，转码，压缩，裁剪，片头片尾，分...](https://github.com/microshow/RxFFmpeg)  - 
* [silencecorner/jre-ffmpeg-apline: Dockerfile (jre8)(https://github.com/fabric8io-images/java) and (ffmpeg)(https://hub.docker.com/r/jrottenbe...](https://github.com/silencecorner/jre-ffmpeg-apline)  - 
* [slhck/ffmpeg-debug-qp: FFmpeg Debug Script for QP Values](https://github.com/slhck/ffmpeg-debug-qp)  - 
* [slhck/ffmpeg-encoding-course: An introduction to FFmpeg and its tools](https://github.com/slhck/ffmpeg-encoding-course)  - 
* [x264 FFmpeg Options Guide - Linux Encoding](https://sites.google.com/site/linuxencoding/x264-ffmpeg-mapping)  - 

## Audio
*Audio libraries, tools, and examples.*

* [ EBU R128 Introduction - Florian Camerer](https://www.youtube.com/watch?v=iuEtQqC-Sqo)  - 
* [Adjust and Normalize Your Music Files with FFMPEG - Make Tech Easier](https://www.maketecheasier.com/normalize-music-files-with-ffmpeg/)  - 
* [Audio Loudness Conversational Actions - Google Developers](https://developers.google.com/assistant/tools/audio-loudness)  - 
* [Audio normalization with ffmpeg using loudnorm (ebur128) filter? bytes and bones](https://bytesandbones.wordpress.com/2017/03/16/audio-nomalization-with-ffmpeg-using-loudnorm-ebur128-filter/)  - 
* [How To Normalize Audio - Why Do It? Everything You Need To Know](https://www.learndigitalaudio.com/normalize-audio)  - 
* [How to Set Audio Levels for Video](https://www.premiumbeat.com/blog/how-to-set-audio-levels-for-video/)  - 
* [Loudness Explained Page | Music Tribe - TC Electronic](https://www.tcelectronic.com/brand/tcelectronic/loudness-explained#googtrans(en|en))  - 
* [Multi Channel Audio codec evaluations](https://tech.ebu.ch/docs/tech/tech3324.pdf)  - 
* [Quick Tutorial: How to Increase Volume in Audacity [2019 Update]](https://www.iskysoft.com/video-editing/how-to-increase-volume-in-audacity.html)  - 
* [ReplayGain - Audacity Forum](https://forum.audacityteam.org/viewtopic.php?t=63067)  - 
* [Standard audio A85-2013](https://www.atsc.org/wp-content/uploads/2015/03/Techniques-for-establishing-and-maintaining-audio-loudness.pdf)  - 
* [hybrik-samples/ebu_r128_audio_normalization.json hybrik/hybrik-samples](https://github.com/hybrik/hybrik-samples/blob/master/Feature%20Examples/Filters/ebu_r128_audio_normalization.json)  - 
* [slhck/ffmpeg-normalize: Audio Normalization for Python/ffmpeg](https://github.com/slhck/ffmpeg-normalize#examples)  - 
* [superpoweredSDK/Low-Latency-Android-iOS-Linux-Windows-tvOS-macOS-Interactive-Audio-Platform: Superpowered Audio, Networking and Cryptographics SDKs. High performance and cross platform on Android, iOS, macOS, tvOS, Linux, Windows and modern web browsers.](https://github.com/superpoweredSDK/Low-Latency-Android-iOS-Linux-Windows-tvOS-macOS-Interactive-Audio-Platform)  - 

## Subtitles & Closed Captions
*Subtitling & Closed Caption libraries, tools, and examples.*

* [BingLingGroup/autosub: Command-line utility to transcribe/translate from video/audio/subtitles to subtitles](https://github.com/BingLingGroup/autosub)  - 
* [Can ffmpeg extract closed caption data - Stack Overflow](https://stackoverflow.com/questions/3169910/can-ffmpeg-extract-closed-caption-data)  - 
* [Caption Inspector](https://github.com/Comcast/caption-inspector)  - 
* [Closed Captions vs. Subtitles and why the Difference is Important - Matinee Multilingual](https://www.matinee.co.uk/blog/closed-captions-vs-subtitles-and-why-the-difference-is-important/)  - 
* [DVB-Sub Output Captions - MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/dvb-sub-output-captions.html)  - 
* [Eyevinn/srt-metadata-extractor](https://github.com/Eyevinn/srt-metadata-extractor)  - 
* [Short-notes on Add subtitle to any video with ffmpeg](https://mahasak.com/short-notes-on-add-subtitle-to-any-video-with-ffmpeg/)  - 
* [Ultimate Guide to Closed Captioning](https://www.3playmedia.com/resources/popular-topics/closed-captioning/)  - 
* [Web Video Text Tracks Format (WebVTT) - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)  - 
* [abinashmeher999/voice-data-extract](https://github.com/abinashmeher999/voice-data-extract)  - 
* [active-video/subtitles](https://github.com/active-video/subtitles)  - 
* [alexherbo2/ffmpeg-sub](https://github.com/alexherbo2/ffmpeg-sub)  - 
* [apm1467/videocr](https://github.com/apm1467/videocr)  - 
* [awslabs/serverless-subtitles](https://github.com/awslabs/serverless-subtitles)  - 
* [cea608-extractor](https://github.com/Comcast/cea-extractor)  - 
* [cea608.js](https://github.com/Dash-Industry-Forum/cea608.js)  - 
* [cessen/subs_extract](https://github.com/cessen/subs_extract)  - 
* [federicocalendino/pysub-parser](https://github.com/federicocalendino/pysub-parser)  - 
* [jnorton001/pycaption-cli: A command line interface for the pycaption module.](https://github.com/jnorton001/pycaption-cli)  - 
* [shawnsky/extract-subtitles: Extract Subtitles From Video](https://github.com/shawnsky/extract-subtitles)  - 
* [statsbiblioteket/tv-subtitle-extraction](https://github.com/statsbiblioteket/tv-subtitle-extraction)  - 
* [xinnjie/extract-subtitle](https://github.com/xinnjie/extract-subtitle)  - 

## HEVC
*HEVC (h265) libraries, tools, examples, and resources.*

* [Apple Got It Wrong: Encoding Specs for HEVC in HLS](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=121878)  - Though I didn't recognize it at first, when Apple released its encoding specifications for HEVC and HLS, they got it wrong, though it took a comment from a true encoding expert to help me realize it.
* [Encoding Live and VOD for HEVC & HLS](https://streaminglearningcenter.com/wp-content/uploads/2018/05/Encoding-for-HEVC-SME-2018-Jan.pdf)  - 
* [Eyevinn/docker-hevc](https://github.com/Eyevinn/docker-hevc)  - 
* [Guide to HEVC/H.265 Encoding and Playback - TechSpot](https://www.techspot.com/article/1131-hevc-h256-enconding-playback/)  - 
* [HEVC Scientific overview](http://iphome.hhi.de/wiegand/assets/pdfs/2012_12_IEEE-HEVC-Overview.pdf)  - 
* [HEVC in HLS: 10 Key Questions for Streaming Video Developers](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=122637&PageNum=2)  - 
* [HEVC. Efficienty](https://ieeexplore.ieee.org/ielx7/76/7372356/07254155.pdf?tp=&arnumber=7254155&isnumber=7372356&ref=)  - 
* [HLS Authoring Update for HEVC](https://devstreaming-cdn.apple.com/videos/wwdc/2017/515vy4sl7iu70/515/515_hls_authoring_update.pdf)  - 
* [Jan Olzer on HLS HEVC](https://www.linkedin.com/pulse/market-significance-apples-adopting-hevc-heres-what-i-jan-ozer)  - 
* [Suggestion for x265's --tune film - Doom9's Forum](https://forum.doom9.org/showthread.php?t=172458)  - 
* [hevc video](https://youtu.be/p6dLZfs0jTY)  - 
* [hevc video part 1](https://www.youtube.com/watch?v=TLNkK5C1KN8&feature=youtu.be)  - 
* [hevc video part 2](https://www.youtube.com/watch?v=V6a1AW5xyAw&feature=youtu.be)  - 
* [multicoreware / x265 / wiki / Home](https://bitbucket.org/multicoreware/x265/wiki/Home)  - 
* [x265 Documentation ](https://x265.readthedocs.io/en/default/)  - 

## Ads
*Ads in streaming video related libraries, tools, examples, and resources.*

* [Eyevinn/adxchange-engine](https://github.com/Eyevinn/adxchange-engine)  - 
* [Eyevinn/vast-info](https://github.com/Eyevinn/vast-info)  - 
* [SCTE-104/35 and Beyond: A Look at Ad Insertion in an OTT World | TvTechnology](https://www.tvtechnology.com/opinions/scte10435-and-beyond-a-look-at-ad-insertion-in-an-ott-world)  - 
* [Understanding Real-time Bidding for AVOD Services - Eyevinn Technology - Medium](https://medium.com/@eyevinntechnology/understanding-real-time-bidding-for-avod-services-861ebfa8bd13)  - 
* [Understanding Server-Side Dynamic Ad Insertion - Eyevinn Technology - Medium](https://medium.com/@eyevinntechnology/understanding-server-side-dynamic-ad-insertion-d7ed90e34aa2)  - 

## Roku
*Roku app tools, libraries,and examples.*

* [CCecilia/roku-suite-desktop: Tool suite for Roku channel development.](https://github.com/CCecilia/roku-suite-desktop)  - 
* [MediaBrowser/Emby.Roku: Emby for Roku](https://github.com/MediaBrowser/Emby.Roku)  - 
* [Playing Videos | Roku Developer](https://developer.roku.com/docs/developer-program/core-concepts/playing-videos.md#PlayingVideos-Examples)  - 
* [Roku Developer | Documentation | Streaming specifications](https://developer.roku.com/docs/specs/streaming.md)  - 
* [Streaming specifications | Roku Developer](https://developer.roku.com/docs/specs/streaming.md#AudioandVideoSupport-AdaptiveBitrateFormats)  - 
* [T-Pham/RokuJSONHelperNode: Roku SceneGraph JSON Helper](https://github.com/T-Pham/RokuJSONHelperNode)  - 
* [Video | Roku Developer](https://developer.roku.com/docs/references/scenegraph/media-playback-nodes/video.md)  - 
* [XML + Code + Good times = RSG Application - Plex Labs - Medium](https://medium.com/plexlabs/xml-code-good-times-rsg-application-b963f0cec01b)  - 
* [anachirino/bifserver: Server which creates and serves up BIF files for Roku players](https://github.com/anachirino/bifserver)  - 
* [briandunnington/Redoku: Redux for Roku](https://github.com/briandunnington/Redoku)  - 
* [briandunnington/Roact: React for Roku](https://github.com/briandunnington/Roact)  - 
* [chrishoffman/brightscript-json: JSON parser for Roku's proprietary Brightscript language](https://github.com/chrishoffman/brightscript-json)  - 
* [dphang/roku-lib: Some useful Roku utilities](https://github.com/dphang/roku-lib)  - 
* [exegersha/network-benchmark: Proof of concept. Roku app implementing network layer using scene graph nodes.](https://github.com/exegersha/network-benchmark)  - 
* [gabek/Amplitude-Brightscript: A Brightscript (Roku) library for submitting analytics to Amplitude](https://github.com/gabek/Amplitude-Brightscript)  - 
* [gabek/SegmentIO-Brightscript: A BrightScript interface to SegmentIO event tracking](https://github.com/gabek/SegmentIO-Brightscript)  - 
* [georgejecook/rooibos: simple, flexible, fun brightscript test framework for roku scenegraph apps](https://github.com/georgejecook/rooibos)  - 
* [juliomalves/roku-libs: BrightScript Utility Libraries](https://github.com/juliomalves/roku-libs)  - 
* [karimkawambwa/roku-framework-example: This is a project to show how the boku-framework by Karim Kawambwa is used](https://github.com/karimkawambwa/roku-framework-example)  - 
* [karimkawambwa/roku-framework: Roku app framework to make app creation easier and structured. Under construction](https://github.com/karimkawambwa/roku-framework)  - 
* [mrkjffrsn/RokuFramework: An opensource Roku framework](https://github.com/mrkjffrsn/RokuFramework)  - 
* [nod/rokumote: osx app for controlling your roku because sometimes your kids lose the remote](https://github.com/nod/rokumote)  - 
* [rkoshak/sensorReporter: A python based service that receives sensor inputs and publishes them over REST (should work with any API but mainly...](https://github.com/rkoshak/sensorReporter)  - 
* [rokucommunity/brighterscript-formatter: A code formatter for BrighterScript (and BrightScript)](https://github.com/RokuCommunity/brighterscript-formatter)  - 
* [rokucommunity/vscode-brightscript-language: A Visual Studio Code extension for Roku's BrightScript language](https://github.com/rokucommunity/vscode-brightscript-language)  - 
* [rokudev/RAF4RSG-sample: sample demonstrating the Roku Advertising Framework in SceneGraph](https://github.com/rokudev/RAF4RSG-sample)  - 
* [rokudev/SDK-Development-Guide](https://github.com/rokudev/SDK-Development-Guide)  - 
* [rokudev/SceneGraphDeveloperExtensions](https://github.com/rokudev/SceneGraphDeveloperExtensions)  - 
* [rokudev/automated-channel-testing: Roku Automated Channel Testing: Selenium-based WebDriver + Robot Framework + Samples](https://github.com/rokudev/automated-channel-testing)  - 
* [rokudev/dolby-audio-sample: A collection of Dolby test content available in different streaming protocols.](https://github.com/rokudev/dolby-audio-sample)  - 
* [rokudev/samples: Collection of sample channels for side-loading on your Roku device](https://github.com/rokudev/samples)  - 
* [rokudev/unit-testing-framework: Tool for automating and testing Roku channels](https://github.com/rokudev/unit-testing-framework)  - 
* [rolandoislas/BrightWebSocket: RFC 6455 WebSocket Library for the Roku](https://github.com/rolandoislas/BrightWebSocket)  - 
* [schtanislau/brightscript-state-machine: State management for Roku channel](https://github.com/schtanislau/brightscript-state-machine)  - 
* [sjbarag/brs-testbed: A simple, buildable Roku channel that executes arbitrary BrightScript files.](https://github.com/sjbarag/brs-testbed)  - 
* [veeta-tv/jasmine-roku: Example jasmine tests using node-roku-test for verifying Roku channel behavior](https://github.com/veeta-tv/jasmine-roku)  - 
* [willowtreeapps/ukor: A Roku build tool with support for build flavors](https://github.com/willowtreeapps/ukor)  - 
* [zype/zype-roku-scenegraph](https://github.com/zype/zype-roku-scenegraph)  - 

## Dolby
*Dolby specs, libraries, examples, and tools.*

* [Dolby Vision for Content Creators | Dolby Laboratories](https://www.dolby.com/us/en/technologies/dolby-vision/dolby-vision-for-creative-professionals.html)  - 
* [Dolby Vision streams within the HTTP Live Streaming format](https://www.dolby.com/us/en/technologies/dolby-vision/dolby-vision-streams-within-the-http-live-streaming-format-v2.0.pdf)  - 
* [DolbyProfessional Loudness](https://www.dolby.com/us/en/technologies/dolby-professional-loudness-solutions.pdf)  - 
* [Hybrik API Reference](https://docs.hybrik.com/api/v1/HybrikAPI.html?#getting-started)  - 
* [hybrik/hybrik-samples](https://github.com/hybrik/hybrik-samples)  - 

## QoE
*QoE & Analytics tools, libraries, and resources.*

* [Collection of VMAF Resources ](https://streaminglearningcenter.com/blogs/collection-of-vmaf-resources.html)  - How VMAF works.
* [JNoDuq/videobench: VMAF PSNR Bitrate Analyzer](https://github.com/JNoDuq/videobench)  - 
* [Netflix/vmaf](https://github.com/Netflix/vmaf/)  - 
* [Quality of Experience in Streaming](https://medium.com/@eyevinntechnology/quality-of-experience-in-streaming-5c25355a4111?source=userActivityShare-94bccb50d11-1559724940&_branch_match_id=664741478927428385)  - 
* [The Challenge to Maintain and Translate Creative Visual Ideas to Everyone’s Viewing Devices](https://medium.com/@eyevinntechnology/the-challenge-to-maintain-and-translate-creative-visual-ideas-to-everyones-viewing-devices-a88e1a841439)  - 
* [Toward A Practical Perceptual Video Quality Metric - Netflix TechBlog - Medium](https://medium.com/netflix-techblog/toward-a-practical-perceptual-video-quality-metric-653f208b9652)  - 
* [VMAF: The Journey Continues - Netflix TechBlog - Medium](https://medium.com/netflix-techblog/vmaf-the-journey-continues-44b51ee9ed12)  - 
* [Video Bench - How to measure your video quality easily](https://medium.com/@jnoduq/video-bench-how-measure-your-video-quality-easily-85a0feb8f6e2)  - 
* [Video Quality Assessment](https://medium.com/@eyevinntechnology/video-quality-assessment-34abd35f96c0?source=userActivityShare-94bccb50d11-1560983815&_branch_match_id=670021582869771680)  - 
* [cta-wave/R4WG20-QoE-Metrics](https://github.com/cta-wave/R4WG20-QoE-Metrics)  - 

## Tools
*Streaming video tools and resources to make life easier.*

* [A Docker container with the video streaming tools you need](https://medium.com/@eyevinntechnology/a-docker-container-with-the-video-streaming-tools-you-need-b8319e98f36a)  - 
* [Aws video media convert docs](https://docs.aws.amazon.com/en_pv/mediaconvert/latest/ug/mediaconvert-guide.pdf#working-with-queues)  - 
* [Batch-Py-Remux](https://github.com/ZaifSenpai/Batch-Py-Remux)  - 
* [Deep Video Analytics](https://github.com/AKSHAYUBHAT/DeepVideoAnalytics)  - 
* [EEL - A simple Proxy Service for JSON Event Transformation and Forwarding](https://github.com/Comcast/eel)  - 
* [Eyevinn/docker-jit-capture](https://github.com/Eyevinn/docker-jit-capture)  - 
* [Eyevinn/docker-serve: A simple Python based HTTP server that sets CORS allow headers. Useful for streaming from files on local computer](https://github.com/Eyevinn/docker-serve)  - 
* [Eyevinn/fmp4-js](https://github.com/Eyevinn/fmp4-js)  - 
* [Eyevinn/pseudo-live-playout](https://github.com/Eyevinn/pseudo-live-playout)  - 
* [Eyevinn/streaming-analyzer](https://github.com/Eyevinn/streaming-analyzer)  - 
* [Eyevinn/toolbox: A set of Docker containers with Streaming tools](https://github.com/Eyevinn/toolbox)  - 
* [Eyevinn/vod-to-live.js](https://github.com/Eyevinn/vod-to-live.js)  - 
* [Go library for mpeg ts](https://github.com/Comcast/gots)  - 
* [Gpac](https://github.com/gpac/gpac)  - 
* [IMF Conversion Utility](https://github.com/DSRCorporation/imf-conversion)  - 
* [Inca - Netflix](https://link.medium.com/Lu3GnIPeg0)  - 
* [Kthulu120/liquid_dl: Liquid-dl is a simple tool for utlities such as FFMPEG, youtube-dl, and scdl. It provides a simple framework with simpl...](https://github.com/Kthulu120/liquid_dl)  - 
* [Mamba](https://github.com/Comcast/mamba)  - 
* [Marcos-A/STRCleaner](https://github.com/Marcos-A/STRCleaner)  - 
* [Multiformat video player, inspection and conversion tool | Switch](http://primary.telestream.net/switch/)  - 
* [Open Broadcaster Software | OBS](https://obsproject.com/)  - 
* [Stream Analyzer - ts analyzer, stream validation, ETSI TR 101 290 | Elecard: Video Compression Guru](https://www.elecard.com/products/video-analysis/stream-analyzer)  - 
* [SwitchMedia MediaHQ - AdEase Server Side Ad Injection (SSAI)](https://www.switch.tv/mediahq/adease/)  - 
* [SwitchMedia MediaHQ - CMS](https://www.switch.tv/mediahq/)  - 
* [SwitchMedia MediaHQ - Live2VOD asset capture and trimmer](https://www.switch.tv/mediahq/live2vod/)  - 
* [alpine-bento-ffmpeg](https://github.com/realeyes-media/alpine-bento-ffmpeg)  - 
* [channel-engine](https://github.com/Eyevinn/channel-engine)  - 
* [coopernurse/nginx-s3-proxy](https://github.com/coopernurse/nginx-s3-proxy)  - 
* [estliberitas/node-thumbnails-webvtt: Video thumbnail generator generating WebVTT spec file](https://github.com/estliberitas/node-thumbnails-webvtt)  - 
* [jkarthic-akamai/ABR-Broadcaster: A real time encoder for Adaptive Bitrate Broadcast](https://github.com/jkarthic-akamai/ABR-Broadcaster)  - 
* [liwf616/awesome-live-stream](https://github.com/liwf616/awesome-live-stream)  - 
* [mar10/wsgidav: A generic and extendable WebDAV server based on WSGI](https://github.com/mar10/wsgidav)  - 
* [minio/minio: MinIO is a high performance object storage server compatible with Amazon S3 APIs](https://github.com/minio/minio)  - 
* [obsproject/obs-studio: OBS Studio - Free and open source software for live streaming and screen recording](https://github.com/obsproject/obs-studio)  - 
* [realeyes-media/alpine-node-video-multitool](https://github.com/realeyes-media/alpine-node-video-multitool)  - 
* [scte35-js](https://github.com/Comcast/scte35-js)  - 
* [video-dev/vtt.js: A JavaScript implementation of the WebVTT specification](https://github.com/video-dev/vtt.js)  - 
* [video-on-demand-on-aws.pdf](https://s3.amazonaws.com/solutions-reference/video-on-demand-on-aws/latest/video-on-demand-on-aws.pdf)  - 
* [watson-developer-cloud/text-to-speech-nodejs](https://github.com/watson-developer-cloud/text-to-speech-nodejs)  - 

## DRM
*DRM tools, documentations, and resources.*

* [Content Protection for HLS with AES-128 Encryption](https://www.theoplayer.com/blog/content-protection-for-hls-with-aes-128-encryption)  - 
* [CrackerCat/video_decrypter](https://github.com/CrackerCat/video_decrypter)  - 
* [Digital Rights Management (DRM) - Everything you need to know](https://bitmovin.com/digital-rights-management-everything-to-know/)  - 
* [Encryption & DRM with Multiple Keys? Unified Streaming](https://docs.unified-streaming.com/documentation/package/multiple-keys.html)  - 
* [HEVC DRM Market Update](https://go.buydrm.com/thedrmblog/hevc-drm-market-update)  - Since time eternal, the streaming industry has toiled with and extolled the virtues of CODECs and their key enablement of the entire digital video experience.
* [HLS Key Specs](https://tools.ietf.org/html/draft-pantos-hls-rfc8216bis-00#section-5.1)  - HLS Key Files
* [Secure Apple HLS streaming using DRM encryption](https://www.wowza.com/docs/how-to-secure-apple-hls-streaming-using-drm-encryption)  - 
* [Securing OTT Content - DRM](https://medium.com/@eyevinntechnology/securing-ott-content-drm-1af2c08fdd31?source=userActivityShare-94bccb50d11-1560983518&_branch_match_id=670020366479331042)  - 
* [aes-decrypter](https://github.com/videojs/aes-decrypter)  - 
* [shengbinmeng/dash-drm](https://github.com/shengbinmeng/dash-drm)  - 

## Testing
*Video streaming testing tools and helpers.*

* [17 Free MPEG-DASH example and HLS m3u8 sample test streams](https://bitmovin.com/mpeg-dash-hls-examples-sample-streams/)  - Collection of publicly available and free MPEG-DASH and HLS examples, test streams and datasets to help you through your development process
* [4K Media | Free Ultra-HD / HDR / HLG / Dolby Vision 4K Video Demos & Samples](https://4kmedia.org/)  - Sample 4K HDR HLG AND Dolby Vision content
* [Automated testing on devices - Netflix TechBlog - Medium](https://medium.com/netflix-techblog/automated-testing-on-devices-fc5a39f47e24)  - 
* [HLS Test Suite From Eurofins Digital Testing - Free HLS Test Streams and Test Cases](https://hlstests.eurofins-digitaltesting.com/)  - 
* [HTTP Live Streaming (HLS) - Artillery.io Docs](https://artillery.io/docs/plugin-hls/)  - 
* [Xiph.org Test Media](https://media.xiph.org/)  - 
* [artilleryio/artillery-plugin-hls](https://github.com/artilleryio/artillery-plugin-hls)  - 
* [bengarney/list-of-streams](https://github.com/bengarney/list-of-streams)  - 
* [video-dev/streams: A repository of shared streams - no media uploads](https://github.com/video-dev/streams)  - 

## Talks and Presentations
*Conference talks and presentations on streaming video .*

* [Advances in HTTP Live Streaming - WWDC 2017](https://developer.apple.com/videos/play/wwdc2017/504/)  - Videos - Apple Developer
* [Demuxed 2015](https://www.youtube.com/watch?v=s661CU6Fvl4&list=PLkyaYNWEKcOcIXrPKRfIK-T9J48J4Vuwk)  - 
* [Demuxed 2016](https://www.youtube.com/watch?v=kEo2TrXm7F4&list=PLkyaYNWEKcOekC2m9Na77G40Lmhb1bnsK)  - 
* [Demuxed 2017](https://www.youtube.com/watch?v=PSdhW-R9u6s&list=PLkyaYNWEKcOfntbMd6KtHhF7qpL9hj6of)  - 
* [Demuxed 2018](https://www.youtube.com/watch?v=bfK_f7GBA8s&list=PLkyaYNWEKcOfARqEht42i1P4kBemzEV2V)  - 
* [Demuxed 2019](https://m.youtube.com/playlist?list=PLkyaYNWEKcOf_C_6W45abNvXMb40xUUqh)  - 
* [Demuxed Podcast](https://www.heavybit.com/library/podcasts/demuxed/)  - 
* [From sysadmin to SRE](https://www.youtube.com/watch?v=lZI51YzIgVE)  - 
* [Video Insiders Podcast](https://thevideoinsiders.simplecast.com/episodes)  - 
* [mhv/2019 Talks](http://mile-high.video/files/mhv2019/)  - 

## Books
*Books on video streaming.*

* [Communicating Pictures - 1st Edition](https://www.elsevier.com/books/communicating-pictures/bull/978-0-12-405906-1)  - 
* [High Efficiency Video Coding (HEVC): Algorithms and Architectures (Integrated Circuits and Systems): Vivienne Sze, Madhukar Budagavi, Gary J...](https://www.amazon.com/gp/product/3319068946/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)  - 
* [High Efficiency Video Coding: Coding Tools and Specification (Signals and Communication Technology): Mathias Wien: 9783662442753: Amazon.com...](https://www.amazon.com/gp/product/3662442752/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)  - 
* [Producing Streaming Video for Multiple Screen Delivery: Jan Lee Ozer: 9780976259541: Amazon.com: Books](https://www.amazon.com/gp/product/0976259540/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)  - 
* [The MPEG-4 Book: Fernando Pereira, Touradj Ebrahimi: 0076092011132: Amazon.com: Books](https://www.amazon.com/MPEG-4-Book-Fernando-Pereira/dp/0130616214/ref=sr_1_1?keywords=mpeg+4+book&qid=1576252504&s=books&sr=1-1)  - 
* [Video Encoding by the Numbers: Eliminate the Guesswork from your Streaming Video: Jan Lee Ozer: 9780998453002: Amazon.com: Books](https://www.amazon.com/Video-Encoding-Numbers-Eliminate-Guesswork/dp/0998453005/ref=pd_bxgy_14_img_2/142-3989735-6086504?_encoding=UTF8&pd_rd_i=0998453005&pd_rd_r=6591968b-e54f-4fb1-8ab8-18e3f2a52f88&pd_rd_w=tWNbP&pd_rd_wg=RtRbb&pf_rd_p=09627863-9889-4290-b90a-5e9f86682449&pf_rd_r=JQP62Z6C5QJR49SEZNHP&psc=1&refRID=JQP62Z6C5QJR49SEZNHP)  - 

## CDN
*Last mile tools, documentations, and resources.*

* [Amazon S3 as Origin Fastly tutorial](https://docs.fastly.com/en/guides/amazon-s3)  - 
* [Delivering Live Streaming Video with CloudFront and AWS Media Services - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/live-streaming.html)  - 
* [Edge Computing with Fastly CDN and Varnish VCL for Authenticated Requests](https://endertech.com/blog/edge-computing-fastly-cdn-varnish-vcl-authenticated-requests)  - 
* [Fastly compared to Amazon CloudFront](https://www.cdnoverview.com/compare/fastly-vs-amazon-cloudfront/)  - 
* [How to use DASH and HLS Adaptive Streaming with AWS S3 and Cloudfront](https://bitmovin.zendesk.com/hc/en-us/articles/115001609634-How-to-use-DASH-and-HLS-Adaptive-Streaming-with-AWS-S3-and-Cloudfront)  - 
* [Lambda@Edge Design Best Practices | Networking & Content Delivery](https://aws.amazon.com/blogs/networking-and-content-delivery/lambdaedge-design-best-practices/)  - 
* [OTT Content Delivery CDN Alternatives](https://medium.com/@eyevinntechnology/ott-content-delivery-cdn-alternatives-cafe75dab71d?source=userActivityShare-94bccb50d11-1560983135&_branch_match_id=670018733519578135)  - 
* [On-Demand and Live Streaming Video with CloudFront - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/on-demand-streaming-video.html)  - 
* [Optimizing High Availability with CloudFront Origin Failover - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html)  - 
* [Tutorial: Creating a Simple Lambda@Edge Function - Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works-tutorial.html)  - 


### Contributing

Please take a quick look at the [contribution guidelines](https://github.com/krzemienski/awesome-video/blob/master/.github/CONTRIBUTING.md) first. If you see a package or project here that is no longer maintained or is not a good fit, please submit a pull request to improve this file. Thank you to all [contributors](https://github.com/krzemienski/awesome-video/graphs/contributors); you rock!!