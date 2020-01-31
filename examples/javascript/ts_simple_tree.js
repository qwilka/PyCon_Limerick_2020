/*
Simple tree class in Typescript.

Commands to build and run:

tsc --target es6 ts_simple_tree.ts
node ts_simple_tree.js

Tested with
tsc Version 3.7.2
node v10.13.0

Copyright © 2020 Stephen McEntee
Licensed under the GNU Affero General Public License v3.0.
See LICENSE file for details:
https://github.com/qwilka/PyCon_Limerick_2020/blob/master/examples/javascript/LICENSE

Includes code sourced from https://github.com/aureooms/js-itertools
Licence https://github.com/aureooms/js-itertools/blob/master/LICENSE
*/
// https://github.com/aureooms/js-itertools/blob/master/js/src/map/chain.js
let iterchain = function* (iterables) {
    for (let iterable of iterables)
        yield* iterable;
};
// cannot use name «Node»
// use error TS2300: Duplicate identifier 'Node'.
class TsNode {
    constructor(name, parent = null, data = { vn_type: "default" }) {
        this.name = name;
        this.parent = parent;
        this.childs = [];
        if (parent !== null) {
            parent.add_child(this);
        }
    }
    *traverse() {
        yield this;
        for (let child of iterchain(this.childs)) {
            yield child;
        }
    }
    [Symbol.iterator]() {
        return this.traverse();
    }
    add_child(newchild) {
        this.childs.push(newchild);
        newchild.parent = this;
    }
    toTextTree(tabLevel = -1) {
        let nodetext = "";
        tabLevel += 1;
        for (let i = 0; i < tabLevel; i++) {
            nodetext += ".   ";
        }
        nodetext += "|---" + this.name + "\n";
        for (let child of this.childs) {
            nodetext += child.toTextTree(tabLevel);
        }
        return nodetext;
    }
}
// TESTS: just set to true|false, require.main===module does not work with Babel
let run_tests = true;
if (run_tests) {
    console.log("Launching tests for ", "__filename");
    runTests();
}
function runTests() {
    let rootnode = new TsNode("root node");
    let node1 = new TsNode("node1 level1", rootnode);
    let node11 = new TsNode("node11 level2", node1);
    let node12 = new TsNode("node12 level2", node1);
    let node13 = new TsNode("node13 level2", node1);
    let node121 = new TsNode("node121 level3", node12);
    let node122 = new TsNode("node122 level3", node12);
    let node2 = new TsNode("node2 (level1)", rootnode);
    let node21 = new TsNode("node21 (level2)", node2);
    let node211 = new TsNode("node211 (level3)", node21);
    let node212 = new TsNode("node212 (level3) parentless");
    node21.add_child(node212);
    node21.add_child(new TsNode("node213 (level3) parentless"));
    let node3 = new TsNode("node3 (level1)", rootnode);
    for (let node of rootnode)
        console.log(node.name); // iterate over tree
    console.log(rootnode.toTextTree());
    //console.log(JSON.stringify(rootnode.toJsTree(), null, 2));
    //console.log(node2.toTextTree());
    //console.log(JSON.stringify(rootnode.toTreeObj(), null, 2)) 
    // let newnode = new TsNode("", null, rootnode.toTreeObj()) // create new tree using Obj from first tree
    // console.log(newnode.toTextTree())
}
