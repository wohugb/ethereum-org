# donate2

您可以使用** Ethereum钱包**来关注基金会捐赠提示框并保持您的独角兽安全。 [下载最新的电子钱包版本][1]并设置钱包。

首先，您可能需要将Unicorn令牌添加到您的观察列表中，因为独角兽有时看不见。
滚动到底部并点击**Watch Token**。
添加地址**0x89205A3A3b2A69De6Dbf7f01ED13B2108B2c43e7**，其余信息将自动加载。,点击*确定*您的令牌将被添加。
现在你需要得到一个！

![隐形独角兽](/images/tutorial/unicorn-token.png)

在同一页面上，向上滚动并点击**Watch contract**。
把**Ethereum基金会提示框**（或任何其他）作为名称，**0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359**作为地址，然后将此代码添加为**界面**：

    [{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"proposals","outputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"},{"name":"description","type":"string"},{"name":"votingDeadline","type":"uint256"},{"name":"executed","type":"bool"},{"name":"proposalPassed","type":"bool"},{"name":"numberOfVotes","type":"uint256"},{"name":"currentResult","type":"int256"},{"name":"proposalHash","type":"bytes32"}],"type":"function"},{"constant":false,"inputs":[{"name":"proposalNumber","type":"uint256"},{"name":"transactionBytecode","type":"bytes"}],"name":"executeProposal","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"memberId","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"numProposals","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"priceOfAUnicornInFinney","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"newUnicornPriceInFinney","type":"uint256"},{"name":"newUnicornAddress","type":"address"}],"name":"changeUnicorn","outputs":[],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"members","outputs":[{"name":"member","type":"address"},{"name":"voteWeight","type":"uint256"},{"name":"canAddProposals","type":"bool"},{"name":"name","type":"string"},{"name":"memberSince","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"debatingPeriodInMinutes","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"minimumQuorum","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"targetMember","type":"address"},{"name":"voteWeight","type":"uint256"},{"name":"canAddProposals","type":"bool"},{"name":"memberName","type":"string"}],"name":"changeMembership","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"beneficiary","type":"address"},{"name":"weiAmount","type":"uint256"},{"name":"JobDescription","type":"string"},{"name":"transactionBytecode","type":"bytes"}],"name":"newProposalInWei","outputs":[{"name":"proposalID","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":true,"inputs":[],"name":"majorityMargin","outputs":[{"name":"","type":"int256"}],"type":"function"},{"constant":true,"inputs":[],"name":"unicornAddress","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":false,"inputs":[{"name":"beneficiary","type":"address"},{"name":"etherAmount","type":"uint256"},{"name":"JobDescription","type":"string"},{"name":"transactionBytecode","type":"bytes"}],"name":"newProposalInEther","outputs":[{"name":"proposalID","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"minimumQuorumForProposals","type":"uint256"},{"name":"minutesForDebate","type":"uint256"},{"name":"marginOfVotesForMajority","type":"int256"}],"name":"changeVotingRules","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"proposalNumber","type":"uint256"},{"name":"supportsProposal","type":"bool"},{"name":"justificationText","type":"string"}],"name":"vote","outputs":[{"name":"voteID","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[{"name":"proposalNumber","type":"uint256"},{"name":"beneficiary","type":"address"},{"name":"amount","type":"uint256"},{"name":"transactionBytecode","type":"bytes"}],"name":"checkProposalCode","outputs":[{"name":"codeChecksOut","type":"bool"}],"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"type":"function"},{"inputs":[{"name":"minimumQuorumForProposals","type":"uint256"},{"name":"minutesForDebate","type":"uint256"},{"name":"marginOfVotesForMajority","type":"int256"},{"name":"congressLeader","type":"address"}],"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"proposalID","type":"uint256"},{"indexed":false,"name":"recipient","type":"address"},{"indexed":false,"name":"amount","type":"uint256"},{"indexed":false,"name":"description","type":"string"}],"name":"ProposalAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"proposalID","type":"uint256"},{"indexed":false,"name":"position","type":"bool"},{"indexed":false,"name":"voter","type":"address"},{"indexed":false,"name":"justification","type":"string"}],"name":"Voted","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"proposalID","type":"uint256"},{"indexed":false,"name":"result","type":"int256"},{"indexed":false,"name":"quorum","type":"uint256"},{"indexed":false,"name":"active","type":"bool"}],"name":"ProposalTallied","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"member","type":"address"}],"name":"MembershipChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"minimumQuorum","type":"uint256"},{"indexed":false,"name":"debatingPeriodInMinutes","type":"uint256"},{"indexed":false,"name":"majorityMargin","type":"int256"}],"name":"ChangeOfRules","type":"event"}]

![观看基金会](/images/tutorial/watch-foundation.png)

这会将它添加到您的观察列表中。
点击它可以进入合同页面，在那里你可以关注基金会如何处理这些捐款。
在左栏中，您可以看到合同上的所有公共信息，例如千分之一秒（也称为“finney”）中的独角兽标记的价格，或者提议在其之前必须保持可见的最少时间,可以执行（目前24小时）。

![密切关注基础尖端罐](/images/tutorial/foundation-tip-box.png)

**在此页面**上，如果您想贡献更多**以太**，请点击顶部的存款以太网按钮并捐赠您想要的任何金额。
如果您发送超过独角兽价格的限制（目前为2.014乙以太），那么您将获得一个或多个独角兽！

![有史以来第一次独角兽令牌交易](/images/tutorial/unicorn-is-born.png)

如果你想发送你的独角兽给其他人，或者甚至可以保存到一个钱包，这很容易：只要去**Send**选项卡，选择你拥有一个独角兽帐户，你的独角兽令牌将出现在,你的“以太”和你拥有的任何其他货币。

[1]: https://github.com/ethereum/mist/releases