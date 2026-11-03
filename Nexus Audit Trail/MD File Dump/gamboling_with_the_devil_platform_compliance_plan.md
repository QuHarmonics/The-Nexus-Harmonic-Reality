# Gamboling with the Devil — Platform and Compliance Production Plan

**Draft date:** April 28, 2026  
**Purpose:** Identify what the production team must know before continuing with a Twitch-led, Restream-distributed live show where the “Devil” / active player is physically in New Jersey and plays legal online casino games while comedians commentate remotely.

> **Important:** This is a production-risk memo, not legal advice. Before launch, retain counsel familiar with New Jersey internet gaming, influencer advertising, platform moderation, and live entertainment contracts.

---

## 1. Executive collapse

The viable structure is:

$$
\boxed{\text{NJ player} + \text{NJ-approved online casino} + \text{Twitch primary stream} + \text{no referral funnel}}
$$

The dangerous structure is:

$$
\Omega = \text{offshore/crypto casino} + \text{casino promo links/codes} + \text{viewer-funded or viewer-controlled wagering}
$$

The **core legal/platform invariant** should be:

> **The player controls all gambling decisions. Viewers, Bits, Stars, Gifts, Super Chats, comments, and comedians may only affect the show/performance layer.**

For a first pilot, the safest path is **Twitch-only or Twitch + carefully configured YouTube**, not full simultaneous restream to every platform. Facebook, Instagram, and TikTok introduce more ambiguity and stricter gambling-promotion risk.

---

## 2. Base legal model: New Jersey wagering

### 2.1 Required wagering location

The active player must be physically located in New Jersey while placing online casino wagers. New Jersey internet gaming rules require location detection and prohibit internet/mobile wagering unless the patron is physically present in New Jersey.

**Operating rule:**

$$
\boxed{\text{The device/account placing wagers must be in New Jersey.}}
$$

### 2.2 Age and account identity

New Jersey internet/mobile gaming requires the operator to verify that the patron is at least **21**, not self-excluded, not on an exclusion list, and not otherwise prohibited from gaming. The patron must acknowledge that the account is for the patron only and that allowing another person to access/use the account is prohibited.

**Production consequence:**

- The player must be **21+**.
- The player must use their own legal account.
- No account sharing.
- No remote control from NYC.
- No remote desktop into an NJ machine.
- No VPN workaround.
- No “the comedians click for him.”
- No macros/bots/automated wagering.

### 2.3 Use only NJ-approved internet gaming sites

The New Jersey Division of Gaming Enforcement states that internet gaming site approvals are issued on a rolling basis and that any site not included on the DGE list is **not approved** to offer internet gaming in New Jersey.

**Operating rule:**

$$
\boxed{\text{Use only a New Jersey DGE-approved internet gaming site.}}
$$

Do not rely on “legal casino lists” from blogs. Use the official DGE approved-site list and take a screenshot/PDF of the approval page for the production folder before each pilot.

### 2.4 Operator terms of service

Even if a casino site is legal in New Jersey, its terms may restrict:

- screen recording,
- livestreaming,
- commercial/public display,
- use of logos/trademarks,
- commentary around the game,
- third-party capture tools,
- account access from unusual network configurations,
- use of overlays or automated input tools.

**Must-do before launch:** obtain written confirmation from the operator or counsel that the planned broadcast does not violate the operator’s terms.

---

## 3. Platform-by-platform compliance map

## 3.1 Twitch — primary platform, best fit

### Status

**Recommended primary platform.** Twitch allows gambling content when properly labeled and when the stream does not use prohibited gambling sites or referral mechanics.

### Must do

- Apply Twitch’s **Gambling** Content Classification Label when real-money gambling is shown or discussed as active stream content.
- Use only gambling sites that are licensed in the U.S. or another jurisdiction Twitch considers to provide sufficient consumer protection.
- Do not stream prohibited/offshore/unsafe gambling sites.
- Do not share links or affiliate codes to sites containing slots, roulette, or dice.
- Do not use chat commands, panels, QR codes, overlays, banners, or verbal CTAs that direct viewers to a casino signup path.
- Do not use Bits as a bet/wager or accept Bits for a bet/wager.
- Keep Bits/subscriptions as show-support and performance-trigger mechanics only.

### Twitch Bits / subs boundary

Twitch’s Bits policy allows Bits for community goals, voting, and content-triggered experiences, but prohibits using Bits as a bet or wager or soliciting/accepting Bits for a bet or wager.

**Allowed structure:**

$$
\text{Bits} \to \text{comedian / Devil prompt} \to \text{performance response}
$$

**Do not build:**

$$
\text{Bits} \to \text{spin / bet / cashout / continue / stop command}
$$

### Twitch subscriber boundary

Paid subscribers are acceptable as normal Twitch channel monetization **if they do not receive gambling influence or gambling upside**.

Safe subscriber benefits:

- emotes,
- badges,
- sub-only chat,
- subscriber Discord,
- behind-the-scenes non-gambling content,
- comedy prompt privileges that do not affect wagering.

Do not offer:

- win shares,
- prize pools tied to gambling outcomes,
- subscriber-only bet control,
- subscriber-only “choose the next wager,”
- subscriber-funded spins.

### Twitch risk rating

**Green/yellow** if the show uses an NJ-approved site, labels the content, avoids casino links/codes, and keeps paid interaction out of wagering control.

---

## 3.2 YouTube — usable, but link/logo/age-risk sensitive

### Status

**Possible secondary platform**, but treat as more restrictive than Twitch for online gambling content.

### Must know

YouTube’s regulated goods policy prohibits content that aims to sell, link to, or facilitate access to uncertified online gambling sites. The policy applies to videos, descriptions, comments, live streams, and external links, including clickable URLs, verbal directions, and other forms of directing users.

YouTube gives examples of prohibited content including:

- facilitating access to an online gambling or sports betting site that is not certified,
- promising guaranteed returns via online gambling, regardless of whether the site is certified.

YouTube also lists as age-restricted content: content that facilitates access to, promotes, or depicts online gambling and social/sweepstakes casinos, including certified sites.

### Production consequence

For YouTube Live/restream:

- Set the stream as **not made for kids**.
- Age-restrict if available/appropriate.
- Do not include casino links in title, description, pinned comments, chatbots, overlays, or verbal calls to action.
- Do not say “sign up,” “use code,” “link below,” or similar.
- Do not promise returns, systems, strategies, or “easy money.”
- Avoid displaying or verbally emphasizing the casino brand unless counsel confirms the operator is Google/YouTube-certified and that showing the interface is acceptable.
- Disable or aggressively moderate chat links.

### YouTube risk rating

**Yellow.** Usable for a sanitized, age-restricted feed, but higher risk if the casino brand/logo/site name is displayed or discussed as a promotional destination.

---

## 3.3 Facebook — possible, but advertising/boosting is restricted

### Status

**Use caution.** Organic/live gambling content rules are less directly stated than the ad rules, but Meta’s advertising rules are strict around online gambling and games.

### Must know

Meta defines online gambling/games as any product or service where anything of monetary value is included as part of entry and prize. Meta says ads that promote online gambling and gaming are only allowed with prior written permission, authorized advertisers must follow applicable laws, and ads must use targeting consistent with Meta’s requirements. At minimum, ads may not target people under 18.

### Production consequence

For Facebook Live/restream:

- Do not boost/promote the stream as an ad without prior written Meta permission.
- Do not run paid ads for the stream unless the ad account is authorized for gambling/gaming promotion and properly age/geo-targeted.
- Do not include casino referral links, affiliate codes, signup CTAs, or promotional claims.
- Treat the feed as 21+ even if Meta’s baseline ad minimum says 18+.
- Use responsible-gaming language.
- Disable or moderate comments containing casino links or referral codes.
- Confirm whether Facebook Live will age-gate/geo-gate the content as needed.

### Facebook risk rating

**Yellow/red** unless kept organic, non-promotional, non-linked, and age/geo-conscious. Paid amplification is a separate approval path.

---

## 3.4 Instagram — high-risk for live casino restreaming

### Status

**Not recommended for the first live casino pilot.** Instagram is better used for edited, non-promotional, non-linking clips after review.

### Must know

Instagram is governed by Meta’s policies. Meta’s ad standards require prior written permission for ads promoting online gambling/games. Branded-content/sponsorship disclosures may also apply if any casino/operator or related brand provides compensation, free play, credits, hotel/travel, or other material value.

### Production consequence

For Instagram Live/restream:

- Avoid live real-money casino restreaming for the first pilot.
- If used, do not promote, link, tag, or direct viewers to casino sites.
- Do not use affiliate codes, QR codes, link stickers, pinned CTAs, or “go sign up” language.
- Do not boost clips without authorization.
- Use only edited clips that clearly frame the show as comedy commentary, not gambling promotion.
- Avoid showing account details, casino deposit screens, cashier pages, or promo pages.

### Instagram risk rating

**Red/yellow.** Safer as a clip-distribution platform than as a simultaneous live casino feed.

---

## 3.5 TikTok — weakest fit for real-money casino restreaming

### Status

**Do not use for the first live real-money casino restream unless you obtain explicit platform/account approval.**

### Must know

TikTok’s gambling ad policy requires certification, limits gambling ads to specified markets where gambling is legal, requires age-appropriate targeting, requires responsible-gambling practices, and prohibits ads that promote unlicensed/illegal gambling, mislead viewers, fail transparency requirements, target underage audiences, or feature underage people.

TikTok Shop policy is stricter: gambling activities are prohibited in TikTok Shop livestreams and videos even if creators do not engage viewers or offer a prize; prohibited examples include casino-style games, roulette, slot machines, wagers, lotteries, and raffles.

### Production consequence

For TikTok:

- Do not restream the live real-money slot feed by default.
- Do not use TikTok Shop features with the show.
- Do not run gambling ads without certification and market approval.
- Do not include casino links, codes, sign-up prompts, or gambling strategy claims.
- Use TikTok for carefully edited, non-promotional show clips only after policy review.

### TikTok risk rating

**Red for live real-money casino restreaming.** Use only after explicit approval/certification or keep it to sanitized non-promotional clips.

---

## 4. Restream-specific considerations

Restream is not the compliance shield. It is only the distribution pipe.

$$
\boxed{\text{Every destination platform still applies its own rules.}}
$$

### 4.1 Strictest-platform rule

When simulcasting the same feed to Twitch, YouTube, Facebook, Instagram, and TikTok, the strictest platform effectively controls the whole feed.

That means a feed that is acceptable on Twitch may still create problems on YouTube, Facebook, Instagram, or TikTok.

### 4.2 Recommended rollout

**Phase 1: Twitch-only pilot**

- Prove format.
- Test moderation.
- Validate NJ casino/operator permissions.
- Validate Bits/subscription boundary.
- Record VOD for legal/platform review.

**Phase 2: Twitch + YouTube**

- Use sanitized lower-risk feed.
- No links/codes.
- Age-restrict where possible.
- Moderate chat aggressively.

**Phase 3: Meta/TikTok clips only**

- Edited clips.
- No casino links/codes.
- No deposit/cashier screens.
- No “go play” language.
- No boosted/paid ads unless approved.

**Do not start with full five-platform live restream.** That creates the largest unresolved policy surface.

### 4.3 Chat aggregation risk

If Restream aggregates chat across platforms, one viewer posting a casino link or code on one platform can cause the link to appear on other platforms.

**Must do:**

- disable link display in overlays,
- block casino URLs,
- block referral-code patterns,
- block offshore casino names,
- block QR-code posts/images,
- use a moderator delay if possible,
- disable cross-platform chat overlay until tested.

---

## 5. Monetization rules

## 5.1 Twitch Bits

Allowed:

$$
\text{Bits} \to \text{comedian behavior / Devil performance / overlay / sound / segment prompt}
$$

Avoid:

$$
\text{Bits} \to \text{wager behavior}
$$

Do not use Bits to:

- fund the bankroll,
- buy spins,
- trigger spins,
- choose bet size,
- choose casino game/slot,
- decide cashout,
- decide stop/go,
- decide deposit amount,
- enter viewers into prize pools,
- split winnings,
- run raffles tied to gambling outcomes.

## 5.2 Twitch subscriptions

Subscriptions can support the channel. Subscription status should not alter gambling decisions or create gambling outcome benefits.

## 5.3 YouTube Super Chats / Super Stickers / memberships

Apply the same boundary:

$$
\text{paid interaction} \to \text{performance layer only}
$$

Do not let Super Chats or memberships influence wagers, bankroll, game selection, or cashout/continue decisions.

## 5.4 Facebook Stars / Instagram gifts / TikTok gifts

Same boundary, plus greater caution because Meta/TikTok gambling promotion risk is higher.

Do not create any mechanic where gifts/stars determine gambling action.

---

## 6. Sponsorships, affiliate links, and disclosure

## 6.1 First pilot recommendation

Do not take casino sponsorship or affiliate money for the first pilot.

Why:

$$
\text{comedy stream} \to \text{casino acquisition funnel}
$$

is the risk transformation that triggers platform scrutiny.

## 6.2 If sponsorship exists

If a casino/operator, affiliate network, or gambling brand provides payment, free play, credits, travel, lodging, comps, or any material benefit, FTC endorsement disclosure rules apply. The disclosure must be clear and conspicuous.

Also, disclosure does **not** override platform gambling rules. A disclosed casino sponsorship can still violate Twitch, YouTube, Meta, or TikTok policies if it includes prohibited links, codes, targeting, or promotional claims.

## 6.3 No referral funnel

Avoid everywhere:

- affiliate links,
- referral codes,
- promo codes,
- QR codes,
- “link in bio,”
- “DM for casino,”
- “use code DEVIL,”
- pinned signup comments,
- chatbot casino commands,
- verbal signup directions,
- operator landing pages,
- deposit instructions.

---

## 7. Content and language restrictions

Avoid these claims across all platforms:

- “guaranteed win,”
- “easy money,”
- “risk-free,”
- “free money,”
- “this system works,”
- “the machine is due,”
- “you can beat this,”
- “deposit now,”
- “go sign up,”
- “use our code,”
- “watch and learn how to win.”

Allowed safer framing:

- “Entertainment only.”
- “No gambling advice.”
- “The player makes all wagering decisions.”
- “Do not gamble if you are under 21 or in a location where it is not legal.”
- “If gambling is a problem, call 1-800-GAMBLER.”

---

## 8. Required on-screen / panel language

Use a small persistent footer:

> **21+ | Entertainment Only | No Gambling Advice | No Links/Codes | Player Controls All Wagers | Gamble Responsibly | 1-800-GAMBLER**

Use a rules panel / pinned statement on Twitch:

> This stream is comedy commentary over legal New Jersey online casino play. The player is 21+ and physically located in New Jersey. Viewers and paid interactions control show prompts only. The player alone controls all gambling decisions. No casino links, referral codes, promo codes, signup instructions, win-sharing, viewer-funded wagers, or gambling advice.

---

## 9. Technical/production controls

### 9.1 Screen capture

- Hide account name, email, address, phone, balance details if not needed, cashier pages, deposit pages, withdrawal pages, tax documents, and geolocation checks.
- Never show payment details.
- Never show full account settings.
- Never show KYC documents.
- Never show casino support chat with personal information.

### 9.2 Moderation

Before going live, configure auto-moderation for:

- links,
- casino URLs,
- referral codes,
- “use code,”
- “VPN,”
- offshore/crypto casino names,
- underage gambling comments,
- “I’m 17 and gambling” type comments,
- self-harm/problem-gambling crisis messages requiring moderator escalation.

### 9.3 Records

Maintain a production compliance folder:

- DGE approved-site screenshot/PDF,
- operator permission/TOS review,
- Twitch labels screenshot,
- platform stream settings screenshots,
- moderation wordlist,
- responsible-gaming footer screenshot,
- player age/location compliance memo,
- sponsorship/disclosure memo,
- VOD archive,
- incident log.

---

## 10. Pre-launch checklist

### Legal / operator

- [ ] Player is 21+.
- [ ] Player is physically in New Jersey.
- [ ] Player uses their own account.
- [ ] Site appears on official NJ DGE approved list.
- [ ] Operator TOS reviewed for streaming/public display/commercial use.
- [ ] Written operator permission obtained or counsel approves proceeding without it.
- [ ] No remote desktop or remote wagering control.
- [ ] No VPN.
- [ ] No offshore/crypto/sweepstakes casino.
- [ ] Stop-loss and session limits set.
- [ ] Responsible-gaming language visible.

### Twitch

- [ ] Gambling Content Classification Label applied.
- [ ] Significant profanity label considered if comics are persistently vulgar.
- [ ] No casino links/codes/promo CTAs.
- [ ] Bits menu affects only performance layer.
- [ ] Subs do not affect gambling decisions or winnings.
- [ ] Chat moderation active.

### YouTube

- [ ] Not made for kids.
- [ ] Age restriction considered/applied if available.
- [ ] No links/codes in description, pinned chat, overlays, or speech.
- [ ] No guaranteed-return claims.
- [ ] Casino logo/brand exposure reviewed.

### Facebook / Instagram

- [ ] No paid ads/boosting unless Meta permission exists.
- [ ] No gambling links/codes.
- [ ] Age/geo restriction options reviewed.
- [ ] Branded content disclosure plan if any value changes hands.
- [ ] Prefer clips over live casino restream for first phase.

### TikTok

- [ ] Do not livestream real-money casino content by default.
- [ ] Do not use TikTok Shop features.
- [ ] No ads without certification/approval.
- [ ] Use only sanitized clips after review.

### Restream

- [ ] Confirm each destination’s policy before adding it.
- [ ] Disable cross-platform chat overlay or heavily moderate it.
- [ ] Disable links in chat overlay.
- [ ] Confirm platform-specific captions/descriptions do not include gambling CTAs.
- [ ] Record locally.

---

## 11. Must-answer questions before continuing

1. **Which exact NJ online casino/operator will be used?**  
   Must be checked against the official NJ DGE approved list.

2. **Does the operator permit commercial livestreaming of its interface/gameplay?**  
   Must be answered from TOS, operator email, or counsel.

3. **Will the casino brand/logo be visible in the feed?**  
   If yes, YouTube/Meta/TikTok risk increases.

4. **Is there any compensation, free play, credits, affiliate relationship, or casino sponsorship?**  
   If yes, FTC disclosure and platform ad/branded-content rules activate.

5. **Will the show use Twitch Bits/subs only, or equivalents on other platforms too?**  
   Any paid interaction must map to performance only, not wagering.

6. **Will the stream be Twitch-only first, or full Restream on day one?**  
   Recommended: Twitch-only first.

7. **Will casino links/codes be banned entirely?**  
   Recommended: yes.

8. **Who is the compliance producer/moderator during the live show?**  
   Someone must have authority to cut feed, mute, block links, or stop the show.

9. **How will problem-gambling comments be handled?**  
   Need a moderator protocol and 1-800-GAMBLER response language.

10. **Who owns the VOD/clips and where will they be reposted?**  
   YouTube, Instagram, Facebook, and TikTok all have different downstream risk.

---

## 12. Recommended launch path

$$
\Delta_1 = \text{Twitch-only pilot}
$$

- NJ player.
- NJ-approved casino.
- No sponsor.
- No links/codes.
- Bits/subs only affect comedians/performance.
- Hard moderation.
- Record local VOD.

$$
\Delta_2 = \text{Review VOD with counsel / platform-risk checklist}
$$

- Identify any problematic language.
- Identify visible logos/URLs/account data.
- Verify moderation worked.
- Edit clip policy.

$$
\Delta_3 = \text{Add YouTube if sanitized}
$$

- No links/codes.
- Age-restrict if available.
- Avoid/crop brand calls to action.

$$
\Delta_4 = \text{Use Meta/TikTok for edited clips only}
$$

- No casino calls to action.
- No deposits/cashier screens.
- No “how to play” or “go play” framing.

---

## 13. Source links reviewed

### New Jersey

- NJ Division of Gaming Enforcement — Internet Gaming Sites: https://www.njoag.gov/about/divisions-and-offices/division-of-gaming-enforcement-home/internet-gaming-sites/
- N.J. Admin. Code § 13:69O-1.2 — General requirements for internet/mobile gaming: https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-13-69O-1-2
- N.J. Admin. Code § 13:69O-1.3 — Internet/mobile gaming accounts: https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-13-69O-1-3

### Twitch

- Twitch Community Guidelines: https://legal.twitch.com/legal/community-guidelines/
- Twitch Content Classification Guidelines: https://safety.twitch.tv/s/article/Content-Classification-Guidelines
- Twitch Content Classification Labels: https://help.twitch.tv/s/article/content-classification-labels
- Twitch unsafe slots/roulette/dice gambling sites policy: https://safety.twitch.tv/s/article/Prohibiting-Unsafe-Slots-Roulette-and-Dice-Gambling-Sites
- Twitch Bits Acceptable Use Policy: https://legal.twitch.com/en/legal/bits-acceptable-use/
- Twitch Monetized Streamer Agreement: https://legal.twitch.com/en/legal/monetized-streamer-agreement/
- Twitch Simulcasting Guidelines: https://help.twitch.tv/s/article/simulcasting-guidelines

### YouTube

- YouTube illegal or regulated goods/services policy: https://support.google.com/youtube/answer/9229611
- YouTube online gambling policy update, March 2025: https://support.google.com/youtube/thread/328728041/an-update-to-youtube%E2%80%99s-policies-on-online-gambling-content
- YouTube online gambling/social casino update, October 2025: https://support.google.com/youtube/thread/383711785/youtube-s-strengthened-approach-to-online-gambling-and-graphic-violence-in-gaming

### Meta / Facebook / Instagram

- Meta Advertising Standards: https://transparency.meta.com/policies/ad-standards/
- Meta Online Gambling and Games ad policy: https://transparency.meta.com/policies/ad-standards/restricted-goods-services/gambling-games/
- Meta Restricted Goods and Services Community Standard: https://transparency.meta.com/policies/community-standards/restricted-goods-services/
- Instagram Branded Content Policies: https://help.instagram.com/1695974997209192

### TikTok

- TikTok Ads — Gambling and Games policy: https://ads.tiktok.com/help/article/tiktok-ads-policy-gambling-and-games
- TikTok Shop Gambling Policy: https://seller-us.tiktok.com/university/essay?knowledge_id=2903157654996737
- TikTok Shop Content Policy: https://seller-us.tiktok.com/university/essay?knowledge_id=6837891779151617

### Restream

- Restream Terms of Service: https://restream.io/terms-of-service

### FTC

- FTC Endorsement Guides FAQ: https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking
- FTC Disclosures 101 for Social Media Influencers: https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers

---

## 14. Bottom-line operating rule

$$
\boxed{\text{NJ controls the wager. Twitch hosts the live show. Restream waits until the feed is sanitized.}}
$$

$$
\boxed{\text{Paid interaction controls comedians, not casino actions.}}
$$

