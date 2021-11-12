class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2
        sum_left, sum_right = 0, 0
        blank_left, blank_right = 0, 0
        for i in range(0, half):
            if num[i] == '?':
                blank_left += 1
            else:
                sum_left += int(num[i])
        
        for i in range(half, len(num)):
            if num[i] == '?':
                blank_right += 1
            else:
                sum_right += int(num[i])
        
        if blank_right >= blank_left:
            blank_right -= blank_left
            blank_left = 0
        else:
            blank_left -= blank_right
            blank_right = 0
        
        if sum_left == sum_right:
            if blank_right + blank_left == 0:
                return False
            else:
                return True
        elif sum_left > sum_right:
            if blank_right == 0:
                return True
            else:
                inc = blank_right // 2
                if blank_right % 2 == 1:
                    return True
                elif sum_left - sum_right == 9 * (blank_right // 2):
                    return False
                else:
                    return True
        else:
            if blank_left == 0:
                return True
            else:
                inc = blank_left // 2
                if blank_left % 2 == 1:
                    return True
                elif sum_right - sum_left == 9 * (blank_left // 2):
                    return False
                else:
                    return True

        
if __name__ == "__main__":
    solution = Solution()
    print(solution.sumGame("528092428757?21586241?5027456449?485625728?70320320742761?70758777121513422849939?08?9?2613715?04165915201777490??509?7?592304501896164236?103?26642147?64925158377674996165?9266108573278?8147617422438649?081081866?179454918?01?72?2601645977?9452321941680061027?7697499564?122031030372368314727601227?7707933496050166799840767899?7308069?581467?1?79576?024375738395?9724?66572934172232971674?33800545228015619318?3745508428910771199180812?135247871255213?7603?754?82?14565328632666?7850?72081155?6260??6029084668455048926738997563410??85628843188??4852008943??4681054851017490?75399893544926?83?158?9357126611062?73?7158698864976776228277288137702?85196?115??940821545447022960443270185106794?9756?7922877725199?663658?07?41209481813989098?378018?204339?7189569070562608564111?8242?24124?6209520046152654610339937??88614?0578617?0630??489138249671?83258238687007?9420074?946539?84028?914161284?63985547435537950209700268?7681180715695620?175370304531943375047930?36?1???498728??3999?21921249384308948706056?641?8775803?0468?75063519?0361?3?32?5411?07??6095431?735058?3??199?71791100651207049?61?10804661963990767699150?7859?3?110919392845?6797232002496854?9822?749545089203880?653?33153779?59959465217073033793375636205?0?15081247395?003342?34258323024?1026153473?552?8961?12233865596?3?0993842530?42?89731791?286857872558777?4969033373634?66?925481?2147853907895??67766575460273415148881431115083535444392840445669078263337389877515366377805?292407553?6668459090225999966361863715974121?8?2097023164334817???058025?6621286716323467299?4938743027?16938597779014?754?69263?2967?629160324841376?81511?85672438070?1?7656?36004125?77?711837274220??9124186210427523083?7?08?1647??090063?35331060?0?53131?220681558393866?133155206?5063?7?3??1?49501364971892419562?525715099?768389030914363?910?2574326303?97?52450864035?533?803396852701713023212983381674?2?336293?4?49734715662776896?27066149828246747?468971?527323008576665674?9160169??236458750663370??502497243992?0116691836264488694611952436?4?02701168646225223?7281?7932302346?79121416?141509377100409?0138069847759655?553566?90551076209184357978630505057397691567164?932898027148727178333?2116025643471?2?8715399156686334141115931952569?0409?83665528993160875243772942095481497374605233?0276420?86567566184?4386125?90472927742333059?12662?01572?01859626301367492617647501111?783099974192?6?7649215182606888718?981312920875102932?184011845?82603?40848729758598831030?32432983954296?184?462671462831?435?98926??2?56?6?0?93141818615155?4?2340163611284971859484?91025625889679240822269??405396?727578446834146511131290148?706827?7881609?3068?538909728?32152850676251538144?7443096?3?48079705097?545?10?52???6501673?59999999999999999999"))