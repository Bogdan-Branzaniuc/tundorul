from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from allauth.socialaccount.models import SocialToken, SocialAccount
import requests
import json


class HandleVods(View):
    def get(self, request, *args, **kwargs):
        """

        """
        vods = {'id': '1817207597', 'stream_id': '46852362636', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 29] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-11T16:28:06Z', 'published_at': '2023-05-11T16:28:06Z', 'url': 'https://www.twitch.tv/videos/1817207597', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/211db826bfcbf075454f_tundorul_46852362636_1683822482//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 36, 'language': 'ro', 'type': 'archive', 'duration': '4h26m0s', 'muted_segments': None}
        {'id': '1816387533', 'stream_id': '46850149708', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 28] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-10T16:30:42Z', 'published_at': '2023-05-10T16:30:42Z', 'url': 'https://www.twitch.tv/videos/1816387533', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/c336237ef5060f45ba6f_tundorul_46850149708_1683736238//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 17, 'language': 'ro', 'type': 'archive', 'duration': '1h25m30s', 'muted_segments': None}
        {'id': '1815549574', 'stream_id': '46848150380', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 27] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-09T16:29:43Z', 'published_at': '2023-05-09T16:29:43Z', 'url': 'https://www.twitch.tv/videos/1815549574', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/dbb7351ac9232cbf5cf3_tundorul_46848150380_1683649776//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 42, 'language': 'ro', 'type': 'archive', 'duration': '2h11m30s', 'muted_segments': None}
        {'id': '1814728873', 'stream_id': '46846031580', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 26] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-08T16:30:21Z', 'published_at': '2023-05-08T16:30:21Z', 'url': 'https://www.twitch.tv/videos/1814728873', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/7d714f05f6459735f03c_tundorul_46846031580_1683563416//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 27, 'language': 'ro', 'type': 'archive', 'duration': '2h54m0s', 'muted_segments': None}
        {'id': '1812084073', 'stream_id': '46838885500', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 25] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-05T16:30:29Z', 'published_at': '2023-05-05T16:30:29Z', 'url': 'https://www.twitch.tv/videos/1812084073', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/81e57d96c9de63a610cb_tundorul_46838885500_1683304224//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 41, 'language': 'ro', 'type': 'archive', 'duration': '2h8m10s', 'muted_segments': None}
        {'id': '1811245746', 'stream_id': '46836770188', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 24] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-04T16:30:35Z', 'published_at': '2023-05-04T16:30:35Z', 'url': 'https://www.twitch.tv/videos/1811245746', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/a7d9817d444127cb2ad7_tundorul_46836770188_1683217829//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 20, 'language': 'ro', 'type': 'archive', 'duration': '2h5m10s', 'muted_segments': None}
        {'id': '1810456575', 'stream_id': '46834714508', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 23] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-03T16:59:41Z', 'published_at': '2023-05-03T16:59:41Z', 'url': 'https://www.twitch.tv/videos/1810456575', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/8f356c9627a14dc1825d_tundorul_46834714508_1683133176//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 24, 'language': 'ro', 'type': 'archive', 'duration': '2h4m50s', 'muted_segments': None}
        {'id': '1809587595', 'stream_id': '46832433452', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 22] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-02T16:30:45Z', 'published_at': '2023-05-02T16:30:45Z', 'url': 'https://www.twitch.tv/videos/1809587595', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/a083f48200bd4ced346c_tundorul_46832433452_1683045040//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 15, 'language': 'ro', 'type': 'archive', 'duration': '2h12m40s', 'muted_segments': None}
        {'id': '1808724362', 'stream_id': '46830136396', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 21] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-01T16:28:22Z', 'published_at': '2023-05-01T16:28:22Z', 'url': 'https://www.twitch.tv/videos/1808724362', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/1b42886513063eb584fd_tundorul_46830136396_1682958496//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 17, 'language': 'ro', 'type': 'archive', 'duration': '2h7m30s', 'muted_segments': None}
        {'id': '1805886941', 'stream_id': '46822344732', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 20] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-28T16:29:46Z', 'published_at': '2023-04-28T16:29:46Z', 'url': 'https://www.twitch.tv/videos/1805886941', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/ade0216237e62490bcfb_tundorul_46822344732_1682699381//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 38, 'language': 'ro', 'type': 'archive', 'duration': '2h26m50s', 'muted_segments': None}
        {'id': '1805025938', 'stream_id': '46820130140', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 19] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-27T16:29:48Z', 'published_at': '2023-04-27T16:29:48Z', 'url': 'https://www.twitch.tv/videos/1805025938', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/191aad0dcd75eef969fc_tundorul_46820130140_1682612983//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 29, 'language': 'ro', 'type': 'archive', 'duration': '3h7m20s', 'muted_segments': None}
        {'id': '1804162393', 'stream_id': '46817709020', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 18] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-26T16:30:34Z', 'published_at': '2023-04-26T16:30:34Z', 'url': 'https://www.twitch.tv/videos/1804162393', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/da8ea2c96ac2df25f76a_tundorul_46817709020_1682526629//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 25, 'language': 'ro', 'type': 'archive', 'duration': '2h45m20s', 'muted_segments': None}
        {'id': '1803295788', 'stream_id': '46815447260', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 17] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-25T16:31:21Z', 'published_at': '2023-04-25T16:31:21Z', 'url': 'https://www.twitch.tv/videos/1803295788', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/8148103de2e126a0faf3_tundorul_46815447260_1682440276//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 22, 'language': 'ro', 'type': 'archive', 'duration': '2h9m50s', 'muted_segments': None}
        {'id': '1802448762', 'stream_id': '46813216556', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 16] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-24T16:31:06Z', 'published_at': '2023-04-24T16:31:06Z', 'url': 'https://www.twitch.tv/videos/1802448762', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/45badf6920c260e58493_tundorul_46813216556_1682353862//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 32, 'language': 'ro', 'type': 'archive', 'duration': '2h8m30s', 'muted_segments': None}
        {'id': '1799725006', 'stream_id': '46806010460', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 15] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-21T16:30:14Z', 'published_at': '2023-04-21T16:30:14Z', 'url': 'https://www.twitch.tv/videos/1799725006', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/02c620d04c071f019f68_tundorul_46806010460_1682094609//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 54, 'language': 'ro', 'type': 'archive', 'duration': '3h40m40s', 'muted_segments': None}
        {'id': '1798860561', 'stream_id': '46803783084', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 14] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-20T16:30:01Z', 'published_at': '2023-04-20T16:30:01Z', 'url': 'https://www.twitch.tv/videos/1798860561', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/d94e4f1c2b0107d905d1_tundorul_46803783084_1682008196//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 22, 'language': 'ro', 'type': 'archive', 'duration': '2h7m40s', 'muted_segments': None}
        {'id': '1798003480', 'stream_id': '46801546412', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 13] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-19T16:30:43Z', 'published_at': '2023-04-19T16:30:43Z', 'url': 'https://www.twitch.tv/videos/1798003480', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/4e5003003eb231b00f9c_tundorul_46801546412_1681921838//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 110, 'language': 'ro', 'type': 'archive', 'duration': '1h49m20s', 'muted_segments': None}
        {'id': '1797134543', 'stream_id': '46799103212', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 12] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-18T16:29:03Z', 'published_at': '2023-04-18T16:29:03Z', 'url': 'https://www.twitch.tv/videos/1797134543', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/2439542090bfbe957b45_tundorul_46799103212_1681835338//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 42, 'language': 'ro', 'type': 'archive', 'duration': '3h41m30s', 'muted_segments': None}
        {'id': '1796281858', 'stream_id': '46796676300', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 11] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-17T16:29:23Z', 'published_at': '2023-04-17T16:29:23Z', 'url': 'https://www.twitch.tv/videos/1796281858', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/47aa8dbbe3ff75c3193c_tundorul_46796676300_1681748958//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 28, 'language': 'ro', 'type': 'archive', 'duration': '2h29m30s', 'muted_segments': None}
        {'id': '1794501541', 'stream_id': '46791635836', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 10] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-15T16:44:46Z', 'published_at': '2023-04-15T16:44:46Z', 'url': 'https://www.twitch.tv/videos/1794501541', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/4b2ac164be3c60334da0_tundorul_46791635836_1681577081//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 23, 'language': 'ro', 'type': 'archive', 'duration': '3h4m0s', 'muted_segments': None}
        {'id': '1792667679', 'stream_id': '46785774460', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 09] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-13T17:02:22Z', 'published_at': '2023-04-13T17:02:22Z', 'url': 'https://www.twitch.tv/videos/1792667679', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/2678a1bc512a51828707_tundorul_46785774460_1681405337//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 18, 'language': 'ro', 'type': 'archive', 'duration': '2h20m50s', 'muted_segments': None}
        {'id': '1790848078', 'stream_id': '46779947580', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 08] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-11T16:01:15Z', 'published_at': '2023-04-11T16:01:15Z', 'url': 'https://www.twitch.tv/videos/1790848078', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/55542bb6a3289f0e577a_tundorul_46779947580_1681228870//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 17, 'language': 'ro', 'type': 'archive', 'duration': '1h56m20s', 'muted_segments': None}
        {'id': '1789989399', 'stream_id': '46777208012', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 07] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-10T15:59:37Z', 'published_at': '2023-04-10T15:59:37Z', 'url': 'https://www.twitch.tv/videos/1789989399', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/cfdc3bf19ff10c215289_tundorul_46777208012_1681142372//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 17, 'language': 'ro', 'type': 'archive', 'duration': '3h6m0s', 'muted_segments': None}
        {'id': '1786314815', 'stream_id': '46766073388', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 06] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-06T16:00:23Z', 'published_at': '2023-04-06T16:00:23Z', 'url': 'https://www.twitch.tv/videos/1786314815', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/c5f1a1224ab7ce896bf4_tundorul_46766073388_1680796818//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 14, 'language': 'ro', 'type': 'archive', 'duration': '1h42m50s', 'muted_segments': None}
        {'id': '1784521994', 'stream_id': '46760417164', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 05] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-04T16:00:21Z', 'published_at': '2023-04-04T16:00:21Z', 'url': 'https://www.twitch.tv/videos/1784521994', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/74edb3ebf1aeec8621d5_tundorul_46760417164_1680624016//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 15, 'language': 'ro', 'type': 'archive', 'duration': '1h39m20s', 'muted_segments': None}
        {'id': '1783627460', 'stream_id': '46757664732', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 04] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-03T15:58:06Z', 'published_at': '2023-04-03T15:58:06Z', 'url': 'https://www.twitch.tv/videos/1783627460', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/d5ee8529335b7f2faa69_tundorul_46757664732_1680537481//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 20, 'language': 'ro', 'type': 'archive', 'duration': '2h21m30s', 'muted_segments': None}
        {'id': '1781799249', 'stream_id': '46752392444', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 03] Ghost of Tsushima', 'description': '', 'created_at': '2023-04-01T16:02:08Z', 'published_at': '2023-04-01T16:02:08Z', 'url': 'https://www.twitch.tv/videos/1781799249', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/f23f9bafbb2b309fe345_tundorul_46752392444_1680364924//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 22, 'language': 'ro', 'type': 'archive', 'duration': '2h49m10s', 'muted_segments': None}
        {'id': '1779925453', 'stream_id': '46746593020', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 02] Ghost of Tsushima', 'description': '', 'created_at': '2023-03-30T16:04:21Z', 'published_at': '2023-03-30T16:04:21Z', 'url': 'https://www.twitch.tv/videos/1779925453', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/1feb39019aa20b6026fa_tundorul_46746593020_1680192256//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 19, 'language': 'ro', 'type': 'archive', 'duration': '2h39m30s', 'muted_segments': None}
        {'id': '1779025014', 'stream_id': '46743980316', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 01] Ghost of Tsushima', 'description': '', 'created_at': '2023-03-29T16:02:31Z', 'published_at': '2023-03-29T16:02:31Z', 'url': 'https://www.twitch.tv/videos/1779025014', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/cd19ec0969d3e9cdb739_tundorul_46743980316_1680105746//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 34, 'language': 'ro', 'type': 'archive', 'duration': '2h40m10s', 'muted_segments': None}
        context = {
            'vods': json.dumps(vods)
        }

        return render(
            request,
            context,
            'vods.html',
        )