## 使用命令行构建智能合约

此页面将帮助您在ethereum命令行上创建*Hello，World*合同。
如果您不知道如何使用命令行，我们建议您跳过本教程，而是使用图形用户界面[1]构建[自定义令牌]。

智能合约是以太坊区块链上的账户持有对象。
它们包含代码功能，可以与其他合同进行交互，制定决策，存储数据并将以太网发送给
合同是由他们的创造者定义的，但是他们的执行，以及他们提供的服务，都是由以太网本身提供的。
只要整个网络存在，它们就会存在并且可执行，并且只有在程序被自毁时才会消失。

你可以用合同做什么？
那么，你几乎可以做任何事情，但是对于我们的入门指南，我们来做一些简单的事情：开始你将创建一个经典的"Hello World"合约，然后你可以建立你自己的加密标记发送给任何哟
一旦你掌握了这一点，那么你将通过众筹筹集资金，如果成功的话，将提供一个完全透明和民主的组织，只会服从自己的公民，永远不会离开
而所有这些都在不到300行的代码中。

在你开始之前：

* [安装以太坊CLI][2]
* [详细了解合同][3]

请在进入`geth`控制台之前确认GUI已关闭。
运行`geth`开始同步过程(第一次运行可能需要一段时间)。

那我们现在就开始吧。

### 你的第一个公民：欢迎你

现在你已经掌握了以太坊的基础知识，让我们进入你的第一个严肃的合同。
前沿是一个很大的开放领土，有时候你可能会感到孤独，所以我们的第一步就是创造一个自动的伴侣，在你感到孤独时迎接你。
我们会称他为"温和"。

Greeter是一个智能数字化实体，它存在于区块链中，并能够根据其输入与任何与之交互的人进行对话。
它可能不是一个讲话者，但它是一个很好的倾听者。
这是它的代码：

```js
    contract Mortal {
        /* 定义类型地址的变量所有者 */
        address owner;

        /* 此功能在初始化时执行并设置合同的所有者 */
        function Mortal() { owner = msg.sender; }

        /* 收回合同资金的功能 */
        function kill() { if (msg.sender == owner) selfdestruct(owner); }
    }

    contract Greeter is Mortal {
        /* 定义类型字符串的变量问候语 */
        string greeting;

        /* 这在合同执行时运行 */
        function Greeter(string _greeting) public {
            greeting = _greeting;
        }

        /* 主功能 */
        function greet() constant returns (string) {
            return greeting;
        }
    }
```

您会注意到此代码中有两个不同的合约：_"凡人"_和_"greeter"_。
这是因为Solidity(我们使用的高级合同语言)具有*继承*，这意味着一个合约可以继承另一个合约的特征。
这对简化编码非常有用，因为合约的通用特征不需要每次重写，并且所有合约都可以用更小，更易读的块编写。
所以，只要声明_greeter是mortal_，你就继承了来自"凡人"合同的所有特征，并且使欢迎代码简单易读。

继承特征_"凡人"_仅仅意味着迎宾合同可以被其所有者杀死，以清理区块链并在不再需要合同时收回锁定在其中的资金。
以太坊中的契约默认为不死的，并且没有所有者，这意味着一旦被部署，作者就没有
部署前请考虑这一点。

### 使用Solc编译器编译您的合同

在您能够部署您的合同之前，您需要两件事情：

1. 编译后的代码
2. 应用程序二进制接口，它是一个定义如何与合约进行交互的JavaScript对象

你可以通过使用Solidity编译器来获得这两个。
如果你还没有安装编译器，你可以：

1. 按照[关于安装Solidity编译器的说明][4]在您的机器上安装编译器
2. 使用基于网络的Solidity IDE [Remix][5]

#### Solc在您的机器上

如果您在机器上安装了编译器，则需要编译合约以获取编译的代码和应用程​​序二进制接口。

    solc -o target --bin --abi Greeter.sol

这将创建两个文件，一个文件包含已编译的代码，另一个文件在名为target的目录中创建应用程序二进制接口。

    $tree
    .
    ├── Greeter.sol
    └── target
       ├── Greeter.abi
       ├── Greeter.bin
       ├── Mortal.abi
       └── Mortal.bin

你会看到有为两个合同创建的文件;,但是由于Greeter包括Mortal，你不需要部署Mortal来部署Greeter。

您可以使用这两个文件来创建和部署合同。

    var greeterFactory = eth.contract(<contents of the file Greeter.abi>)

    var greeterCompiled = "0x" + "<contents of the file Greeter.bin>"

你现在编译了你的代码，并将它提供给Geth。
现在您需要准备好进行部署，这包括设置一些变量，例如您希望使用的问候语。
将下面的第一行编辑为比"Hello World！"更有趣的内容,并执行这些命令：

```js
var _greeting = "Hello World!"

var greeter = greeterFactory.new(_greeting,{from:eth.accounts[0],data:greeterCompiled,gas:47000000}, function(e, contract){
    if(e) {
        console.error(e); // If something goes wrong, at least we'll know.
        return;
    }

    if(!contract.address) {
        console.log("Contract transaction send: TransactionHash: " + contract.transactionHash + " waiting to be mined...");

    } else {
        console.log("Contract mined! Address: " + contract.address);
        console.log(contract);
    }
})
```

#### 运用Remix

如果你没有安装Solc，你可以简单地使用在线IDE。
将源代码(在本页顶部)复制到[Remix][5]，它会自动编译你的代码。
您可以放心地忽略右侧任何黄色警告框。

要访问已编译的代码，请确保右窗格中的下拉菜单选择了"greeter"。
然后点击直接在下拉菜单右侧的**Details**按钮。
在弹出窗口中，向下滚动并复制**WEB3DEPLOY**文本框中的所有代码。

在您的计算机上创建一个临时文本文件并粘贴该代码。
确保将第一行更改为如下所示：

    var _greeting = "Hello World!"

现在您可以将结果文本粘贴到geth窗口中，或者使用`loadScript("yourFilename.js")`导入文件。
等待30秒钟，你会看到这样的消息：

    Contract mined! address: 0xdaa24d02bad7e9d6a80106db164bad9399a0423e

您可能必须使用您在开始时选择的密码来"解锁"发送交易的帐户，因为您需要支付部署合同的燃料费用：例如， ,`personal.unlockAccount(web3.eth.accounts [0]，"yourPassword")`。

该合同估计需要约18万个燃料部署(根据[在线固体编译器][6])，在撰写本文时，测试网上的燃料售价为20 gwei([相当于(20000000000 wei，,或0.00000002以太][7])每单位燃料。
有很多有用的数据，包括最新的燃料价格[在网络统计页面][8]。

**请注意，这些费用不会支付给[以太坊开发者][9]，而是转到_Miner_，那些计算机正在努力寻找新块并保证网络安全的同伴。燃料价格由当前计算供需市场决定。如果燃料价格太高，你可以成为矿工并降低你的要价。**

在不到一分钟的时间内，你应该有一个合同地址的日志，这意味着你已经成功地部署了你的合同。
您可以使用以下命令来验证已部署的代码(将被编译)：

    eth.getCode(greeter.address)

如果它返回`0x`以外的任何内容，那么恭喜！
你的小家伙活着！
如果再次创建合同(通过执行另一个eth.sendTransaction)，它将发布到新地址。

### 运行Greeter

为了打电话给你的机器人，只需在终端上输入以下命令：

    greeter.greet();

由于此通知在区块链上没有任何变化，因此它会立即返回并且无需任何燃气费用。
你应该看到它返回你的问候语：

    'Hello World!'

#### 让其他人与您的代码进行交互

为了让其他人来执行你的合同，他们需要两件事情：

1. 合同所在的`address`
2. ABI(应用程序二进制接口)，这是一种用户手册，描述合约功能的名称以及如何将它们调用到您的JavaScript控制台

要获得"地址"，请运行以下命令：

    greeter.address;

要获得`ABI`，运行这个命令：

    greeterCompiled.greeter.info.abiDefinition;

**Tip:**如果你使用[Remix][5]编译代码，上面的代码最后一行不适合你！,相反，您需要直接从Remix中复制`ABI`，类似于您复制** WEB3DEPLOY**编译代码的方式。
在右侧窗格中，单击**Details**按钮并向下滚动到**ABI**文本框。
点击复制按钮复制整个ABI，然后将其粘贴到临时文本文档中。

然后，您可以实例化一个可用于在连接到网络的任何计算机上调用合同的JavaScript对象。
在下面一行中，替换`ABI`(一个数组)和`Address`(一个字符串)来在JavaScript中创建一个契约对象：

    var greeter = eth.contract(ABI).at(Address);

这个特殊的例子可以通过简单地调用来实例化：

    var greeter2 = eth.contract([{constant:false,inputs:[],name:'kill',outputs:[],type:'function'},{constant:true,inputs:[],name:'greet',outputs:[{name:'',type:'string'}],type:'function'},{inputs:[{name:'_greeting',type:'string'}],type:'constructor'}]).at('greeterAddress');

当然，`greeterAddress`必须替换为您合同的_unique_地址。

#### 自己清理

你必须非常高兴才能签下第一份合同，但当业主继续写下更多的合同时，这种激动有时会消失，导致在区块链上看到放弃合同的不愉快景象。
未来，区块链租金可能会实施以增加区块链的可扩展性，但现在，成为一个好公民并且人道地放弃您的废弃机器人。

交易将需要发送到网络，并在下面的代码运行后支付区块链所做更改的费用。
自毁是由网络补贴的，所以它的成本比平常的交易要低得多。

    greeter.kill.sendTransaction({from:eth.accounts[0]})

这只能由合同所有者发送的交易触发。
您可以验证该行为是否完成，只需查看是否返回0即可：

    eth.getCode(greeter.address)

请注意，每个合同都必须执行自己的kill子句。
在这种特殊情况下，只有创建合同的账户才能杀死它。

如果你不添加任何杀人条款，它可能永远独立于你和任何地球上的边界而永远活着，所以在你开始生活之前，请检查你的当地法律对此的看法，包括对技术出口的任何可能限制，言论限制以及,任何关于公民权利的立法
人道地对待你的机器人。

[1]: ./token
[2]: https://ethereum.org/cli
[3]: https://github.com/ethereum/go-ethereum/wiki/Contracts-and-Transactions
[4]: http://solidity.readthedocs.io/en/develop/installing-solidity.html
[5]: https://remix.ethereum.org
[6]: https://ethereum.github.io/browser-solidity/
[7]: http://ether.fund/tool/converter#v=20&u=Gwei
[8]: https://stats.ethdev.com
[9]: ../foundation