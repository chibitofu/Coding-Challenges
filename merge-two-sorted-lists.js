/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    var l3 = new Array();
    
    var spliceLists = function(t1, t2) {
        if (t1.next != null) {
            l3.push(t1.val);
            l3.push(t2.val);
            
            return spliceLists(t1.next, t2.next)
        } else {

            l3.push(t1.val);
            l3.push(t2.val);
            
            return l3
        }
    }

    console.log(spliceLists(l1, l2))
};
