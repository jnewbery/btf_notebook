import argparse
from collections import defaultdict
import os
from pprint import pprint
import shutil
import tempfile

from test_framework.blocktools import (create_block, create_coinbase)
from test_framework.mininode import (
    CInv,
    NetworkThread,
    NodeConn,
    NodeConnCB,
    mininode_lock,
    msg_block,
    msg_getdata,
)
from test_framework.test_framework import BitcoinTestFramework
from test_framework.util import (
    PortSeed,
    assert_equal,
    check_json_precision,
    connect_nodes,
    p2p_port,
    wait_until,
)

class ExampleTest(BitcoinTestFramework):
    def set_test_params(self):
        self.setup_clean_chain = True
        self.num_nodes = 3

    def setup_network(self):
        self.setup_nodes()

        connect_nodes(self.nodes[0], 1)
        self.sync_all([self.nodes[0:1]])

def setup_test(self, srcdir):
    self.options = argparse.Namespace

    self.options.nocleanup=False
    self.options.noshutdown=False
    self.options.srcdir = srcdir
    self.options.cachedir = os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + ".cache")
    self.options.loglevel = "INFO"
    self.options.trace_rpc = False
    self.options.coveragedir = None
    self.options.pdbonfailure = False

    PortSeed.n = os.getpid()
    os.environ['PATH'] = srcdir + ":" + os.environ['PATH']

    check_json_precision()

    # Set up temp directory and start logging
    self.options.tmpdir = tempfile.mkdtemp(prefix="test")
    self._start_logging()

    self.setup_chain()
    self.setup_network()

def shutdown_test(self, cleanup=True):
    self.log.info("Stopping nodes")
    if self.nodes:
        self.stop_nodes()

    self.log.info("Nodes stopped")

    if cleanup:
        self.log.info("Cleaning up log directory")
        try:
            shutil.rmtree(self.options.tmpdir)
        except FileNotFoundError:
            self.log.info("Log directory not found")
    else:
        self.log.info("Not cleaning up dir %s" % self.options.tmpdir)
